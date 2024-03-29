#https://codeclubprojects.org/en-GB/python/iss/ <---ISS



#!/bin/python3

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url)
result = json.loads(response.read())
people = result['people']
#print(result)

#print(people)

print('People in Space: ', result['number'])

for p in people:
  print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('latitude: ', lat)
print('longitude:', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

#Step 3
