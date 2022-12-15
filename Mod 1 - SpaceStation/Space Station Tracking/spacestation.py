#!/bin/python3

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
  print(p['name'], 'in', p['craft'])
  
  
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(145)

iss.penup()
iss.goto(lon, lat)