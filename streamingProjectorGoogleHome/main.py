# from controller.serverController.server_controller import server_controller
# from server import index

# class main_class:
#     def __init__(self):
#         self.sc = server_controller()
#         index.start_server()

# main_class()

from flask import Flask
from flask import request
from server.middleware import middleware

mid = middleware()

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run()

