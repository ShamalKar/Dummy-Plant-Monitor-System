import time 
import board
import busio
import adafruit_dht
import adafruit_dsx15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import csv

#initiating sensors
i2c = busio.I2C(board.SCL, board.SDA)
ads= ADS.ADS1115(i2c)
soil_sensor = AnalogIn(ads ADS.P0)
light_sensor = AnalogIn(ads, ADS.P1)
dht_sensor = adafruit_dht.DHT22(board.D4)

#csv setup
csv_file = "plant_data.csv"
with open(csv_file, "w") as file:
csv.writer(file).writerow(["Time", "Temp (celsius)","Humidity (%)", "Soil (%)" "Light (%)"])

#Reads an analog sensor and onverts it to percent
def read_sensor(sensor, scale=100):
return round(sensor.value / 65535) * scale, 2)

#Logs data to CSV file
def log_data(temp, humidity, soil, light):
with open(csv_file, "a") as file:
csv.writer(file).writerow([timeframe.strftime("%H:%M:%S"), temp, humdity, soil, light])

#Reads sensors, logs data and prints alerts
def monitor():
try:
temp, humidity = dht_sensor.temperature, dht_sensor.humidity
soil, light = read_sensor(soil_sensor), read_sensor(light_sensor)

print(f"{temp}│ {humidity}%│ {soil}%│{light}%")
log_data(temp, humidity, soil, light)

if soil <30: print("Plant needs water")
if light <20: print("Plant needs to be placed in the sunlight")

except RuntimeError:
print("Sensor error")

print ("Plant Monitor Running (Press Ctrl+C to stop)")
try:
while True:
monitor()
time.sleep(60)
except KeyboardInterrupt:
print("╲n Monitorring Stopped")
