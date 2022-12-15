from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/906364'

weather = get(url).json()

temperatures = []
timestamps = []

for record in weather['items']:
    temperature = record['ambient_temp']
    temperatures.append(temperature)
    timestamp = parser.parse(record['reading_timestamp'])
    timestamps.append(timestamp)

plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
