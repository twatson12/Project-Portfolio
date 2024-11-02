import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
import time

def scan_port(target_ip: str, port: int, timeout: float = 1.0) -> tuple[int, bool]:
    """
    Scan a single port on the target IP address.
    Returns tuple of (port number, boolean indicating if port is open)
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        result = sock.connect_ex((target_ip, port))
        is_open = result == 0
    except socket.error:
        is_open = False
    finally:
        sock.close()
        
    return port, is_open

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Simple port scanner for network diagnostics')
    parser.add_argument('target', help='Target IP address to scan')
    parser.add_argument('-p', '--ports', help='Port range (e.g. 20-100)', default='1-1024')
    parser.add_argument('-t', '--threads', type=int, help='Number of threads', default=50)
    args = parser.parse_args()
    
    # Parse port range
    start_port, end_port = map(int, args.ports.split('-'))
    ports = range(start_port, end_port + 1)
    
    print(f"\nScanning {args.target} for open ports...")
    start_time = time.time()
    
    # Scan ports using thread pool
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_port = {
            executor.submit(scan_port, args.target, port): port 
            for port in ports
        }
        
        open_ports = []
        for future in future_to_port:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                print(f"Port {port}: Open")
    
    duration = time.time() - start_time
    print(f"\nScan completed in {duration:.2f} seconds")
    print(f"Found {len(open_ports)} open ports")
    if open_ports:
        print("Open ports:", ", ".join(map(str, sorted(open_ports))))

if __name__ == '__main__':
    main()