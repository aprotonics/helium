import json
from helium import *
from selenium.webdriver import ChromeOptions


url  = "https://httpbin.io/ip"
url2 = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

options = ChromeOptions()
options.add_argument('--proxy-server=52.188.28.218:3128')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
start_chrome(url2, options=options)

all_texts = find_all(Text())
all_text_fields = find_all(TextField())

tle_text = all_texts[0].value

print(len(all_texts))
print()

tle_text_obj = json.loads(tle_text)

kill_browser()


file = "/home/time_traveller/macros/scripts/cdh/mars_data.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
    f.write(tle_text)
