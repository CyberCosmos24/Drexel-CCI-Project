#!/bin/bash
echo "1 - PortScanner"
echo "2 - IP-Lookup"
echo "Enter the tool you want to use"

read user

case user in 
    1) python3 PortScanner/pscan.py
    2) python3 IP-Info/lookup.py