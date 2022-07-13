



import socket  


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# or host
target = input('What you want to scan?: ')
 
# next line gives us the ip address
# of the target
ip = socket.gethostbyname(target)
print('Starting scan on host:', ip)
 
# function for scanning ports
 
 
def port_scan(port):
    try:
        s.connect((ip, port))
        return True
    except:
        return False
 


for port in range(8080):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

