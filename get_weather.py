import requests
from app import env_variables
# from datetime import date, datetime
# base_date = ''.join(str(date.today()).split("-"))
# base_time = datetime.now().strftime("%H00")

service_key = env_variables["openweather_key"]
lat = env_variables["lat"]
lon = env_variables["lon"]


def call_weather(lat=lat, lon=lon):
  url = 'https://api.openweathermap.org/data/2.5/weather'
  params = {'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'kr', 'appid': service_key}
  response = requests.get(url, params=params)
  weather = response.json()["weather"][0]
  return {'weather_id': weather["id"]}

# print(call_weather())