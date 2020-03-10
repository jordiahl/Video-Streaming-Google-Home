import json
import pathlib
from flask import Response
from flask import Request
from flask import json
from flask import jsonify
from pydialogflow_fulfillment import DialogflowRequest


class middleware:
    def get_root(self, req):
        hello = {"hel": "hello"}
        return json.jsonify(hello)

    def post_root(self, req: Request):
        print("this is my req " + str(req.json))
        return req.json

    def post_google_api(self, req: Request):
        # dialog_fulfillment = DialogflowRequest(req.data)
        # print(dialog_fulfillment.get_intent_name())
        # request = req.get_json()
        # responseId = request['responseId']
        # print("this is my response ID")
        # print(responseId)
        # print("this is my req to the google api ")
        # print(request)
        self.format_response()
        return jsonify({'res': req.get_json()})


    def format_response(self):
        pathToFile=pathlib.Path(__file__).parent
        completePath = pathToFile.joinpath('google_api_response.json') 

        dialog_flow_response=''
        with open(completePath) as f:
            dialog_flow_response = json.load(f)
        print("this is my json response--------------------------------------------------------")
        print(dialog_flow_response)
        response_json = json.jsonify(dialog_flow_response) 
        return response_json
        













