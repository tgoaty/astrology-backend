from geopy import Nominatim
from immanuel import charts
from models import NatalData


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
        arr.append(str(object))
    return arr
