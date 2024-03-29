#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

## Define APOD

apodurl = 'https://api.nasa.gov/planetary/apod?'
#mykey = 'api_key=DEMO_KEY'  ## your key goes in place of DEMO_KEY
mykey = 'api_key=cqwBNilE8tkZfj2eT8UCdkaKJTjhq3I1tMA0Sohd'

## Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

##decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeapod)

## use firefox to open the HTTPS URL
input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])
