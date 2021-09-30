# save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    return {"word": word}

if __name__ == "__main__":
    """
    with this check we ensure that we are on the main app file
    and we could run the app with the command below with the command python main.py

    If we haven't specify, we've to type this command instead : 
    env FLASK_APP=main.py flask run
    """
    app.run(host="0.0.0.0", port=5050)
    # With host at 0.0.0.0 we could call our app for all ip adress related to our server (here it could be localhost:5050 or 127.0.07:5050 or <private_ip_address>:5050)