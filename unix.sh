#!/bin/bash
echo "1 - PortScanner"
echo "2 - IP-Lookup"
echo "3 - Geolocation-IP"
echo "4 - Brute Password Cracker"
echo "5 - Brute Hash Cracker"
echo "6 - Wordlist Password Cracker"
echo "7 - Wordlist Hash Cracker"
echo "8 - HTTP-Requests"
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
    python3 PasswordCracker/brute-password.py
    ;;

  5)
    python3 PasswordCracker/brute-hash.py
    ;;
  6) 
    python3 PasswordCracker/wordlist-password.py 
    ;;
  7)
    python3 PasswordCracker/wordlist-hash.py
    ;;
  8)
    python3 HTTP-Requests/request.py
    ;;
  *)
    echo "Enter a vaild tool number"
    ;;
esac
