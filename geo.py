from openrouteservice import client
import os
from geopy.geocoders import Nominatim
import pprint

client = client.Client(key=os.getenv('ORS_API_KEY'))
coordinate_buffer = dict()


def coordinates(city):
    if city in coordinate_buffer:
        return coordinate_buffer[city]
    else:
        geolocator = Nominatim(user_agent='team-fahrtkosten')
        location = geolocator.geocode(city)
        coordinate_buffer[city] = (location.longitude, location.latitude)
        return location.longitude, location.latitude


def distance(city0, city1):
    route = client.directions(
        coordinates=[coordinates(city0), coordinates(city1)],
        profile='driving-car',
        instructions=False,
        format='geojson')
    return route['features'][0]['properties']['summary']['distance']
