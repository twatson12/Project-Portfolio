Packet Analyzer
===============

A comprehensive Python script that captures and analyzes network traffic in real-time, providing detailed statistics on protocols, IP addresses, and ports.

Table of Contents
-----------------

-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Statistics](#statistics)

Features
--------

-   Captures network packets at the Ethernet layer.
-   Analyzes packet headers to extract protocol, IP, and port information.
-   Updates statistics on total packets, protocol distribution, top IP addresses, and top ports.
-   Prints periodic traffic analysis reports.

Installation
------------

1.  **Clone the repository**:

    bash

    Copy code

    `git clone https://github.com/your_username/packet-analyzer.git`

2.  **Navigate to the project directory**:

    bash

    Copy code

    `cd packet-analyzer`

3.  **Requirements**:

    -   Ensure you have Python 3 installed.
    -   Run the script with root privileges to capture packets (required on most systems).

Usage
-----

To start capturing and analyzing packets on a specific network interface, use the following command:

bash

Copy code

`sudo python PacketAnalyzer.py`

### Arguments

-   **interface**: Specify the network interface to capture packets on (default is `eth0`). Modify within the code if needed.

### Example Usage

Start packet capture on the default interface:

bash

Copy code

`sudo python PacketAnalyzer.py`

Statistics
----------

The script provides real-time statistics, updated every 10 seconds, including:

-   **Total Packets Captured**: The cumulative number of packets captured since the script started.
-   **Protocol Distribution**: A breakdown of packet counts by protocol (e.g., TCP, UDP, ICMP).
-   **Top 10 IP Addresses**: The most active IP addresses observed in the capture.
-   **Top 10 Ports**: The most frequently used ports, with service names for common ports.

### Sample Output

yaml

Copy code

`=== Traffic Analysis Report ===
Total Packets Captured: 5000

Protocol Distribution:
  TCP: 3000 packets
  UDP: 1500 packets
  ICMP: 500 packets

Top 10 IP Addresses:
  192.168.1.1: 200 packets
  192.168.1.2: 150 packets

Top 10 Ports:
  Port 80 (http): 500 packets
  Port 443 (https): 300 packets`
