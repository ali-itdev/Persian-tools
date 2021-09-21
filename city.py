"""
get_data() 
    to find json files and return it as a python dict.

cities_key()
    return all cities object key in a python list

city_location_by_key()
    return only city location by object key argument

city_details_by_key()
    return a city details including 
    { "en","fa","ckb","ar","latitude","longitude","elevation" }

"""

import json
from __init__ import SETTINGS



def get_data(file_path: str):
    f = open(file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data

def cities_key():
    data = get_data(SETTINGS['cities_path'])
    city = data['ir']['cities']
    key_list = []
    for i in city.keys():
        key_list.append(i)
    return key_list

def city_location_by_key(obj_key):
    data = get_data(SETTINGS['cities_path'])
    location = {}
    data = data['ir']['cities']
    for key in data:
        if key == obj_key:
            city = data[key]
            location.update({"long": city['longitude']})
            location.update({"lat": city['latitude']})
            location.update({"elevation": city['elevation']})
            return location
        return location

def city_details_by_key(obj_key: str):
    data = get_data(SETTINGS['cities_path'])
    data = data['ir']['cities']
    for key in data:
        if key == obj_key:
            return data[key]
    return {}