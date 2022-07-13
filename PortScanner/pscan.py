



import socket  

import sys

 

target = input('What you want to scan?: ')

ip = socket.gethostbyname(target)
print('Starting scan on host:', ip)
 
# function for scanning ports
 
 
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
        print("\n Hostname not correct")
        sys.exit()
except socket.error:
        print("\ Server not working")
        sys.exit()

