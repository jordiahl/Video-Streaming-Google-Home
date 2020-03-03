from flask import Flask
from flask import request
from flask import json
from server.middleware import middleware

app = Flask(__name__)

mid = middleware()


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        return mid.get_root(request)
    if request.method == "POST":
        return mid.post_root(request)


@app.route("/google-api", methods=["POST"])
def google_api():
    if request.method == "POST":
        return mid.post_google_api(request)

def start_server():
    app.run(host= '192.168.1.51', port=62000)