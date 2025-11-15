from helium import *
import json


start_chrome('https://ssd-api.jpl.nasa.gov/periodic_orbits.api?sys=mars-phobos&family=resonant&jacobimin=3&stabmax=1&branch=21')

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

kill_browser()
