from helium import *
import json


start_chrome('https://tle.ivanstanojevic.me/api/tle/48272/propagate')

all_texts = find_all(Text())
all_text_fields = find_all(TextField())


tle_text = all_texts[0].value

print(all_texts)
print(len(all_texts))
print()

tle_text_obj = json.loads(tle_text)

print(type(tle_text_obj))
print(len(tle_text_obj))
print()

for value in tle_text_obj:
    print(value)

print()

gps_coordinates = []

now = tle_text_obj["parameters"]["date"]
satellite_id = tle_text_obj["parameters"]["satelliteId"]

latitude = tle_text_obj["geodetic"]["latitude"]
longitude = tle_text_obj["geodetic"]["longitude"]
altitude = tle_text_obj["geodetic"]["altitude"]

day = now.split("T")[0]

gps_coordinates.append(latitude)
gps_coordinates.append(longitude)
gps_coordinates.append(altitude)

print(day)

for coordinate in gps_coordinates:
    print(coordinate)


kill_browser()
