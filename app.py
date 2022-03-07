from dotenv import load_dotenv

load_dotenv()

import os

env_variables = {
    "port": os.getenv("PORT"),
    "lat": os.getenv("BASE_LAT"),
    "lon": os.getenv("BASE_LON"),
    "openweather_key": os.getenv("SERVICE_KEY"),
    "spotify_id": os.getenv("SPOTIFY_CLIENT_ID"),
    "spotify_secret": os.getenv("SPOTIFY_CLIENT_SECRET"),
}

from flask import Flask, jsonify, redirect, render_template, request
import requests
from pymongo import MongoClient
from bcrypt import checkpw, hashpw

db_client = MongoClient("localhost", 27017)
db = db_client.sunny

service_key = env_variables["openweather_key"]
base_lat = env_variables["lat"]
base_lon = env_variables["lon"]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/join", methods=["POST"])
def join():
    data = request.form
    username = data["username"]
    password = data["password"]
    password2 = data["password2"]
    existing_user = db.sunny.find_one({"username": username})
    if existing_user:
        return jsonify({"ok": False, "err": "이미 존재하는 사용자명입니다."})
    elif password != password2:
        return jsonify({"ok": False, "err": "패스워드가 동일하지 않습니다."})
    else:
        hashed_password = hashpw(password, 5)
        doc = {"username": username, "password": hashed_password}
        db.sunny.insert_one(doc)
        return jsonify({"ok": True})


@app.route("/login", methods=["POST"])
def login():
    data = request.form
    username = data["username"]
    password = data["password"]
    user = db.sunny.find_one({"username": username})
    if not user:
        return jsonify({"ok": False, "err": "존재하지 않는 사용자명입니다."})
    elif password != checkpw(password, user["password"]):
        return jsonify({"ok": False, "err": "잘못된 비밀번호입니다."})
    else:
        return redirect("/", 200)


@app.route("/get-weather", methods=["POST"])
def weather_info():
    # position info를 담아서 보내는 걸 실행하도록 해야 한다.
    pos = request.json
    lat = pos["lat"]
    lon = pos["lon"]
    print(pos)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat or base_lat,
        "lon": lon or base_lon,
        "units": "metric",
        "lang": "kr",
        "appid": service_key,
    }
    response = requests.get(url, params=params)
    weather = response.json()["weather"]
    return jsonify({"weather": weather})


# , ssl_context="adhoc"
if __name__ == "__main__":
    app.run("0.0.0.0", env_variables["port"] or 3333, True)
