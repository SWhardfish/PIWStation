#!/usr/bin/python

import urllib2
import urllib
import os
import time
import datetime
import glob
from time import strftime
import commands
import math
import config

# Humidity Variable
os.system('./hum1.sh')
hum_sensor = '/home/pi/hum_sensor.txt'
print hum_sensor

# *****Humidity*****
def humRead():
     t = open(hum_sensor, 'r')
     lines = t.readlines()
     t.close()

     hum_output = lines[1].find('Humidity=')
     if hum_output != -1:
        hum_string = lines[1].strip()[hum_output+9:]
        hum_c = float(hum_string)
     return round(hum_c,3)

# *****Dewpoint*****
def dewpRead():
     temp = tempFRead()
     print temp
     hum = humRead()
     print hum

     tempc = (temp-32) * 5/9
     dewp_output = tempc - ((100 - hum)/5)
     dewpF = dewp_output * 9/5 + 32
     if dewpF != -1:
        return round(dewpF,3)

# *****Pressure Variable*****
os.system('./pres1.sh')
pres_sensor = '/home/pi/pres_sensor.txt'
print pres_sensor

def presInchRead():
     t = open(pres_sensor, 'r')
     lines = t.readlines()
     t.close()

     pres_output = lines[1].find('Pressure=')
     if pres_output != -1:
        pres_string = lines[1].strip()[pres_output+9:]
        pres_c = float(pres_string)
# Correction to Pressure +10
        pres_corr = (pres_c) * 0.02953  #removed +10 correction
     return round(pres_corr,3)

def tempFRead():  #Fahrenheit
    t = open(pres_sensor, 'r')
    lines = t.readlines()
    t.close()

    temp_output = lines[0].find('Temp=')
    if temp_output != -1:
        temp_string = lines[0].strip()[temp_output+5:]
        temp_c = float(temp_string)*9/5+32
    return round(temp_c,3)


# Weather Underground Upload
while True:
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print datetimeWrite
    data = {}
    data['ID'] = config.stationid 
    data['PASSWORD'] = config.stationkey 
    data['dateutc'] = datetimeWrite
    data['tempf'] = tempFRead()
    data['dewptf'] = dewpRead()
    data['humidity'] = humRead()
    data['baromin'] = presInchRead()
    data['action'] = 'updateraw'
    url_values = urllib.urlencode(data)
    print url_values
    url = 'http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php'
    full_url = url + '?' + url_values
    try:
        print "Writing to WU..."
        # Execute the WU command
        data = urllib2.urlopen(full_url)
        print "Write Complete"

    except:
        # Rollback in case there is any error
        print "Failed writing to WU"


    break
