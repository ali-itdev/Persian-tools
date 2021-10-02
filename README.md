# Persian Tools

## Province

Access iran cities and towns locations

#### Province.city

- cities_key() # return all cities object key in a python list

- city_location_by_key() # return only city location by object key argument

- city_details_by_key() # return a city details including { "en","fa","ckb","ar","latitude","longitude","elevation" }

```
from province import city
from province import district

cities = city.cities_key()

# Locations
for key in cities:
    location = city.city_location_by_key(key)
    print('**********')
    print(key + ' : ')
    print(location)

# Details => fa_key (persian object key)
fa_keys = []
for key in cities:
    detail = city.city_details_by_key(key)
    fa_keys.append(detail['fa'])

    # print('**********')
    # print(key + ' : ')
    # print(detail)

for key in fa_keys:
    locations = district.search_by_fa_key(key)
    print(locations)

```

#### Province.districts

```
from province import district

districts = district.districts_key()

# Towns in a given district key
towns = []

for key in districts:
    town = district.towns_list_by_district_key(key)
    towns.append(town)

print(towns)

```

## Yearbook

Work with gregorian , jalali and hijri calendar

- get_events(day: int, month: int) # Return a list of gregorian , jalali and hijri events

- gregorian_to_hijri(day, month, year = this_year) # Return an object (The year is set by default to the current year)

- gregorian_to_hijri(day, month, year = this_year) # Return an object (The year is set by default to the current year)

- is_leap(year: int, type: str = 'g') # Check for the leap years only in jalali and gregorian

```
import yearbook as yb

gregorian_day = 27
gregorian_month = 9

print(
    yb.is_leap(2021) # False
)

print(
    yb.is_leap(1399,'j') # True
)

print(
    yb.gregorian_to_jalali(gregorian_day, gregorian_month) # {'year': 1400, 'month': 7, 'day': 5}
)

print(
    yb.gregorian_to_hijri(gregorian_day, gregorian_month) # {'year': 1443, 'month': 2, 'day': 20}
)


file = open('r.txt', 'w')

file.writelines(
    str(
        yb.get_events(gregorian_day, gregorian_month)
    )
)

file.close()

```
