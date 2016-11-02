from flask import Flask, send_from_directory
from flask import request
import json


app = Flask(__name__, static_url_path='')

@app.route('/app/<path:path>')
def send_js(path):
    return send_from_directory('Web/app', path)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user", methods=['POST'])
def registerUser():
    postData = json.loads(request.data)
    return "User " + postData["firstname"] + " you are registered."

@app.route("/bike")
def registerBike():
    return "Bike is registered..."

if __name__ == "__main__":
    app.run()