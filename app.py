from dotenv import load_dotenv
load_dotenv()

import os
env_variables = {
  "port": os.getenv("PORT"),
  "lat": os.getenv("BASE_LAT"),
  "lon": os.getenv("BASE_LON"),
  "openweather_key": os.getenv("SERVICE_KEY"),
  "spotify_id": os.getenv("SPOTIFY_CLIENT_ID"),
  "spotify_secret": os.getenv("SPOTIFY_CLIENT_SECRET")
}

from flask import Flask, jsonify, render_template, request
import requests

service_key = env_variables["openweather_key"]
lat = env_variables["lat"]
lon = env_variables["lon"]


def call_weather(lat=lat, lon=lon):
  url = 'https://api.openweathermap.org/data/2.5/weather'
  params = {'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'kr', 'appid': service_key}
  response = requests.get(url, params=params)
  weather = response.json()["weather"][0]
  return {'weather_id': weather["id"]}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-weather", methods=["POST"])
def weather_info():
    # position info를 담아서 보내는 걸 실행하도록 해야 한다.
    body = request.json
    #lat = body["lat"]
    #lon = body["lon"]
    print(body)
    info = call_weather()
    return jsonify(info)


if __name__ == "__main__":
    app.run("0.0.0.0", env_variables["port"] or 3333, True, ssl_context="adhoc")
