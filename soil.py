import os
from dotenv import load_dotenv
import time
import requests

from adafruit_seesaw.seesaw import Seesaw
from board import SCL, SDA
import busio

#load locally stored enviroment variables
load_dotenv()

PLANT_URL = os.environ.get("PLANT_URL")
AUTH_TOKEN  = os.environ.get("TOKEN")

i2c_bus = busio.I2C(SCL,SDA)

soil_sensor = Seesaw(i2c_bus, addr=0x36)

url = PLANT_URL
auth_token = AUTH_TOKEN
 
touch = soil_sensor.moisture_read()
temp = soil_sensor.get_temp()
soil_moisture_percentage = "{0:.0%}".format(touch/1000)
soil_temperature_percentage = "{0:.0%}".format(temp/100)
data = {'soil_moisture': soil_moisture_percentage, 'soil_temperature': soil_temperature_percentage}
requests.patch(url, data, headers = {'Authorization': auth_token})
print(soil_moisture_percentage)



