import os
from dotenv import load_dotenv
load_dotenv()
PORT = os.getenv("PORT")

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", PORT or 3333, True)