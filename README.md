# PIWstation
Raspberry PI Weather Station

This code is for a Raspberry PI Zero Wireless based weather station for measuring temperature, humidity and pressure. The data will be uploaded and displayed on the Weather Underground weather service https://www.wunderground.com  

## Requirements
* Raspberry PI Zero Wireless (the code should work on most if not all PI models)  
* DHT22 humidity sensor  
* BME280 pressure sensor (the one I use does not provide humidity capability)  
* Raspbian: Linux raspberrypi 4.9.35+ #1014 Fri Jun 30 14:34:49 BST 2017 armv6l GNU/Linux  
* Python version: 2.7.9  


## Sensor Drivers
DHT22: https://github.com/adafruit/Adafruit_Python_DHT  
BME280: https://github.com/adafruit/Adafruit_Python_BME280  

## Connecting the Sensors to the PI
DHT22: The Data Pin (normally pin 2) should be connected to PI GPIO 17 (pin 11).
BME280: The Data Pins SDA pin should be connected to PI GPIO 2 (pin 3) and SCL to GPIO 3 (pin 5).

## Installation Instruction
1. Install Raspbian, enable SSH and I2C and connect it to a network.  
2. Install the sensor drivers for both DHT22 and BME280 under /home/pi and as user PI.  
3. Install this package: `git clone https://github.com/SWhardfish/PIWstation.git`

4. Move the downloaded `AdafruitDHT.py` from `/home/pi` to `/home/pi/Adafruit_Python_DHT` which contains modifications to the output format of the DHT22 sensor reading.  
5. Move the downloaded `Adafruit_BME280_Example.py` from `/home/pi` to `/home/pi/Adafruit_Python_GPIO` which contains modifications to the output format of the BME280 sensor reading.
6. Create a user (free) at Weather Underground https://www.wunderground.com/signup.
7. Add a Personal Weather Stations and record the `Station ID` and `Station Key`.
8. Add `Station ID` and `Station Key` to the `config.py` file under `/home/pi`.
9. Add the following line `* * * * * /home/pi/PIWstation.py` the Crontab by typing `crontab -e`. It will read the sensors and upload the readings to Weather Underground every one minute.
10. Go to your Weather Underground personal weather station url and enjoy the uploaded sensor readings.

## Credits
To Tony DiCola (Adafruit Industries) for providing the sensor drivers.
