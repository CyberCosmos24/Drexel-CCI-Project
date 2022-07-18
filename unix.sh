#!/bin/bash
echo "1 - PortScanner"
echo "2 - IP-Lookup"
echo "3 - Geolocation-IP"
echo "4 - Brute-Force"
echo "5 - Brute-Hash"
echo "6 - HTTP-Requests"
echo "Enter the tool you want to use: "
read tool;
case $tool in
  1)
    python3 PortScanner/pscan.py
    ;;

  2)
    python3 IP-Info/lookup.py
    ;;

  3)
    python3 IP-Info/geo-ip.py
    ;;

  4)
    python3 PasswordCracker/brute-force.py
    ;;

  5)
    python3 PasswordCracker/brute-hash.py
    ;;
    
  6)
    python3 HTTP-Requests/request.py
    ;;

  *)
    ;;
esac
