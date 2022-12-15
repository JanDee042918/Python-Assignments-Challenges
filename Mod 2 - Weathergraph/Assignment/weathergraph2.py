from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/552355'

weather = get(url).json()
data = weather['items']

pages = 1

while 'next' in weather and pages < 9:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1

temperatures = []
timestamps = []
humidities = []
soiltemperatures = []

for record in data:
    temperature = record['ambient_temp']
    temperatures.append(temperature)
    timestamp = parser.parse(record['reading_timestamp'])
    timestamps.append(timestamp)
    humid = record['humidity']
    humidities.append(humid)
    soiltemperature = record['ground_temp']
    soiltemperatures.append(soiltemperature)

plt.plot(timestamps, temperatures)
plt.plot(timestamps, soiltemperatures)
plt.plot(timestamps, humidities)
location = 0
legend = True
plt.legend(["Air Temperature", "Soil Temperature",  "Humidity"], loc=0, frameon=legend)
plt.ylabel('Levels ')
plt.xlabel('Date and Time')
plt.show()
