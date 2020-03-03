from flask import Response
from flask import Request
from flask import json
from flask import jsonify


class middleware:
    def get_root(self, req):
        hello = {"hel": "hello"}
        return json.jsonify(hello)

    def post_root(self, req: Request):
        print("this is my req " + str(req.json))
        return req.json

    def post_google_api(self, req: Request):
        responseId = req.get_json()['responseId']
        print("this is my req to the google api " + responseId)
        return jsonify({'res': req.get_json()})