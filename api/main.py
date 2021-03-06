from json import load
import os
from requests import get
from flask import Flask, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random/"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and insert ther UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": "Client-ID "+UNSPLASH_KEY
    }

    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    """
    with this check we ensure that we are on the main app file
    and we could run the app with the command below with the command python main.py

    If we haven't specify, we've to type this command instead : 
    env FLASK_APP=main.py flask run
    """
    app.run(host="0.0.0.0", port=5050)
    # With host at 0.0.0.0 we could call our app for all ip adress related to our server (here it could be localhost:5050 or 127.0.07:5050 or <private_ip_address>:5050)