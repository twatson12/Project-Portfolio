Port Scanner
============

A Python script for network diagnostics that scans open ports on a target IP address, utilizing multithreading to speed up the scanning process.

Table of Contents
-----------------

-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Arguments](#arguments)

Features
--------

-   Scans a specified range of ports on a target IP.
-   Detects and displays open ports.
-   Allows customizable port range and number of threads.
-   Utilizes multithreading for faster scanning.

Installation
------------

1.  Clone the repository:

    bash

    Copy code

    `git clone https://github.com/twatson12/port-scanner.git`

2.  Navigate to the project directory:

    bash

    Copy code

    `cd port-scanner`
    

Usage
-----

To scan for open ports on a target IP, run the script with the following command:

bash

Copy code

`python port_scanner.py <target_ip> [-p port_range] [-t threads]`

Arguments
---------

-   **target_ip**: The IP address you want to scan.
-   **-p, --ports**: Port range to scan, formatted as `start-end` (default: `1-1024`).
-   **-t, --threads**: Number of threads for concurrent scanning (default: `50`).

### Example Usage

1.  Basic scan with default settings:

    bash

    Copy code

    `python port_scanner.py 192.168.1.1`

2.  Specify a custom port range and number of threads:

    bash

    Copy code

    `python port_scanner.py 192.168.1.1 -p 20-80 -t 100`

* * * * *
