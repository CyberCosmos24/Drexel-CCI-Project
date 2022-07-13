import os
import urllib.request
import json
from urllib import *
from platform import system
import sys
from datetime import datetime
import time



ip=input(" Enter IP Address :  ")
url = ("http://ip-api.com/json/")
response = urllib.request.urlopen(url + ip)
data = response.read()
values = json.loads(data)
print("\n IP          : \033[1;32m " + values['query'])
print(" Status      : \033[1;32m " + values['status'])
print(" Region      : \033[1;32m " + values['regionName'])
print(" Country     : \033[1;32m " + values['country'])
print(" Date & Time : \033[1;32m " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(" City        : \033[1;32m " + values['city'])
print(" ISP         : \033[1;32m " + values['isp'])
print(" Lat,Lon     : \033[1;32m " + str(values['lat']) + "," + str(values['lon']))
print(" ZIPCODE     : \033[1;32m " + values['zip'])
print(" TimeZone    : \033[1;32m " + values['timezone'])