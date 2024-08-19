from geopy import Nominatim
from immanuel import charts
from models import NatalData
import json


def get_natal_description(data: NatalData):
    geolocator = Nominatim(user_agent="city_info")
    location = geolocator.geocode(data.city)

    from datetime import datetime

    native = charts.Subject(
        date_time=datetime(int(data.year), int(data.month), int(data.day), int(data.hour), int(data.minute), 0),
        latitude=float(location.latitude),
        longitude=float(location.longitude),
    )
    natal = charts.Natal(native)
    arr = []
    for object in natal.objects.values():
        arr.append([object.name, object.sign.number, object.house.number])

    with open('./data/Houses.json', 'r', encoding='windows-1251') as f:
        houses = json.load(f)
    with open('./data/Signs.json', 'r', encoding='windows-1251') as f:
        signs = json.load(f)

    result = {}
    signs_description = []
    houses_description = []
    houses_keys = houses.keys()
    signs_keys = signs.keys()
    for item in arr:
        planet_name = item[0]
        if planet_name in signs_keys:
            signs_description.append(signs[planet_name][item[1] - 1])
        if planet_name in houses_keys:
            houses_description.append(houses[planet_name][item[2] - 1])

    result["Планеты и точки в Знаках"] = signs_description
    result["Планеты и Точки в Домах"] = houses_description
    return result
