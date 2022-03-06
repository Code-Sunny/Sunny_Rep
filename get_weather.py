from datetime import date
import requests
import os
from dotenv import load_dotenv
from datetime import date, datetime

load_dotenv()

service_key = os.getenv("SERVICE_KEY")
lat = os.getenv("BASE_LAT")
lon = os.getenv("BASE_LON")
base_date = ''.join(str(date.today()).split("-"))
base_time = datetime.now().strftime("%H00")
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'kr', 'appid': service_key}

response = requests.get(url, params=params)
print(response.content)