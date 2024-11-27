import socket
import struct
import datetime
import threading
from collections import defaultdict
import ipaddress

class PacketAnalyzer:
    def __init__(self):
        # Statistics storage
        self.packet_count = 0
        self.protocol_stats = defaultdict(int)
        self.ip_stats = defaultdict(int)
        self.port_stats = defaultdict(int)
        
        # Lock for thread-safe statistics updates
        self.stats_lock = threading.Lock()
        
    def start_capture(self, interface='eth0'):
        """Start capturing and analyzing network traffic."""
        # Create raw socket
        try:
            self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
            self.sock.bind((interface, 0))
        except PermissionError:
            raise PermissionError("This script requires root privileges to capture packets")
            
        print(f"Starting packet capture on interface {interface}...")
        self._capture_loop()
    
    def _capture_loop(self):
        """Main packet capture loop."""
        while True:
            try:
                packet = self.sock.recvfrom(65535)[0]
                self._analyze_packet(packet)
            except KeyboardInterrupt:
                print("\nStopping packet capture...")
                break
            except Exception as e:
                print(f"Error processing packet: {e}")
                continue
    
    def _analyze_packet(self, packet):
        """Analyze a single packet and update statistics."""
        with self.stats_lock:
            self.packet_count += 1
            
            # Parse Ethernet header
            eth_length = 14
            eth_header = packet[:eth_length]
            eth = struct.unpack('!6s6sH', eth_header)
            eth_protocol = socket.ntohs(eth[2])
            
            # Parse IP header
            if eth_protocol == 8:  # IPv4
                ip_header = packet[eth_length:20+eth_length]
                iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                version_ihl = iph[0]
                protocol = iph[6]
                s_addr = socket.inet_ntoa(iph[8])
                d_addr = socket.inet_ntoa(iph[9])
                
                # Update protocol statistics
                protocol_name = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(protocol, str(protocol))
                self.protocol_stats[protocol_name] += 1
                
                # Update IP statistics
                self.ip_stats[s_addr] += 1
                self.ip_stats[d_addr] += 1
                
                # Parse TCP/UDP header for port information
                if protocol in (6, 17):  # TCP or UDP
                    ip_length = (version_ihl >> 4) * 4
                    port_header = packet[eth_length+ip_length:eth_length+ip_length+4]
                    ports = struct.unpack('!HH', port_header)
                    self.port_stats[ports[0]] += 1  # Source port
                    self.port_stats[ports[1]] += 1  # Destination port
    
    def get_statistics(self):
        """Return current traffic statistics."""
        with self.stats_lock:
            stats = {
                'total_packets': self.packet_count,
                'protocols': dict(self.protocol_stats),
                'top_ips': dict(sorted(self.ip_stats.items(), key=lambda x: x[1], reverse=True)[:10]),
                'top_ports': dict(sorted(self.port_stats.items(), key=lambda x: x[1], reverse=True)[:10])
            }
        return stats
    
    def print_statistics(self):
        """Print current traffic statistics in a formatted way."""
        stats = self.get_statistics()
        
        print("\n=== Traffic Analysis Report ===")
        print(f"Total Packets Captured: {stats['total_packets']}")
        
        print("\nProtocol Distribution:")
        for protocol, count in stats['protocols'].items():
            print(f"  {protocol}: {count} packets")
        
        print("\nTop 10 IP Addresses:")
        for ip, count in stats['top_ips'].items():
            print(f"  {ip}: {count} packets")
        
        print("\nTop 10 Ports:")
        for port, count in stats['top_ports'].items():
            service = socket.getservbyport(port) if port < 1024 else "unknown"
            print(f"  Port {port} ({service}): {count} packets")

def main():
    analyzer = PacketAnalyzer()
    
    # Start a thread for statistics printing
    def print_stats_periodically():
        while True:
            try:
                analyzer.print_statistics()
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                threading.Event().wait(10)  # Print stats every 10 seconds
            except KeyboardInterrupt:
                break
    
    stats_thread = threading.Thread(target=print_stats_periodically)
    stats_thread.daemon = True
    stats_thread.start()
    
    # Start packet capture
    analyzer.start_capture()

if __name__ == "__main__":
    main()