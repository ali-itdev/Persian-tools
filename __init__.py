import json

SETTINGS = {
    'default_path': './public/city',
    'cities_path': './public/city/cities.json',
    'districts_path': './public/city/districts.json',
    'formatted': False
}

def get_data(file_path: str):
    f = open(file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data