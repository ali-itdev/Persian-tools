import json

SETTINGS = {
    'default_path': 'perian_tools/public',
    'cities_path': 'perian_tools/public/city/cities.json',
    'districts_path': 'perian_tools/public/city/districts.json',
    'calendar_path': 'perian_tools/public/calendar', 
    'formatted': False
}


def get_data(file_path: str):
    f = open(file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data
