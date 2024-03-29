#!/usr/bin/env python3

import time
import turtle
import urllib.request
import json

## Trace the ISS = earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted.  Press ENTER to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

## My Location
redlat = 47.6 
redlon = -122.3
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('red')
mylocation.goto(redlon, redlat)
mylocation.dot(5)
mylocation.hideturtle()


lon = round(float(lon))
lat = round(float(lat))
#iss.penup()
#iss.goto(lon, lat)

passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(redlat) + '&lon=' + str(redlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))

## print(result) ## uncomment to see the downloaded result

over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)


iss.penup()
iss.goto(lon, lat)

turtle.mainloop()

