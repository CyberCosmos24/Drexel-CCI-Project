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
print("\n IP          : " + values['query'])
print(" Status      :  " + values['status'])
print(" Region      : " + values['regionName'])
print(" Country     : " + values['country'])
print(" Date & Time :  " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(" City        : " + values['city'])
print(" ISP         :  " + values['isp'])
print(" Lat,Lon     :  " + str(values['lat']) + "," + str(values['lon']))
print(" ZIPCODE     :  " + values['zip'])
print(" TimeZone    :  " + values['timezone'])