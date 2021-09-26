import json

SETTINGS = {
    'default_path': './public',
    'cities_path': './public/city/cities.json',
    'districts_path': './public/city/districts.json',
    'calendar_path': './public/calendar', 
    'formatted': False
}


def get_data(file_path: str):
    f = open(file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data
