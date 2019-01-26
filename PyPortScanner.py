#!/usr/bin/env python

from socket import *
import sys
import time
from datetime import datetime

target_host = ""
min_thershold = 1
max_thershold = 100

def scan_target(target_host, port, error_code = 1):
    try:
        sockets = socket(AF_INET, SOCK_STREAM)
        code = sockets.connect_ex((target_host, port))

        if code == 0:
            error_code = code
        sockets.close()
    except Exception as e:
        pass
    return error_code

try:
    target_host = input("[+] Please enter the Target Host: ")
except KeyboardInterrupt:
    print("\n\n[-] Process was interrupted by the User")
    print("[-] Program will shut down now.")
    sys.exit(1)

target_ip = gethostbyname(target_host)
print("\n[+] Host Name: %s Targeted IP: %s" % (target_host, target_ip))
print("[+] Scan Timestamp %s: \n" % (time.strftime("%H:%M:%S:%Y")))
starting_point = datetime.now()

for port in range(min_thershold, max_thershold):
    try:
        outcome = scan_target(target_host, port)

        if outcome == 0:
            print("[*] Port %d is Open" % (port))
    except Exception as e:
        pass
stop_point = datetime.now()
overall_scan_time = stop_point - starting_point
print("\n [+] Scanning is Finished after %s time" % (overall_scan_time))
print("[+]Now exiting. See you next time!! Bye!!")