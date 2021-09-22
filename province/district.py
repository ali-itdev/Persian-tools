from __init__ import SETTINGS, get_data


def districts_key():
    data = get_data(SETTINGS['districts_path'])
    key_list = []
    for i in data.keys():
        key_list.append(i)
    return key_list


def towns_list_by_district_key(district_obj: str):
    data = get_data(SETTINGS['districts_path'])
    key_list = []
    for key in data:
        if key == district_obj:
            for i in data[key].keys():
                key_list.append(i)
    return key_list
