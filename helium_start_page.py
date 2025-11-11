from helium import *
import json


start_chrome('https://tle.ivanstanojevic.me/api/tle/48272')

all_texts = find_all(Text())
all_text_fields = find_all(TextField())


tle_text = all_texts[0].value

print(all_texts)
print(len(all_texts))
print()

print(tle_text)
print()

tle_text_obj = json.loads(tle_text)
print(tle_text_obj)
print()

print(type(tle_text_obj))
print(len(tle_text_obj))
print()

for value in tle_text_obj:
    print(value)

print()

print(tle_text_obj["satelliteId"])
print()












print(len(all_text_fields))
print()


kill_browser()
