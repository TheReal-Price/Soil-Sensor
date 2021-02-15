import time
import requests

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw


i2c_bus = busio.I2C(SCL,SDA)

soil_sensor = Seesaw(i2c_bus, addr=0x36)

url = 'https://soiltracker.herokuapp.com/api/plants/a7634a20-2464-45e7-b44c-840019b359de/'

touch = soil_sensor.moisture_read()
temp = soil_sensor.get_temp()
soil_moisture_percentage = "{0:.0%}".format(touch/1000)
soil_temperature_percentage = "{0:.0%}".format(temp/100)
data = {'soil_moisture': soil_moisture_percentage, 'soil_temperature': soil_temperature_percentage}
requests.patch(url, data, headers = {'Authorization': 'Token 68d23e5ba451de5d66a58d4e8bbe80995d11aa4e'})
print(soil_moisture_percentage)
    

