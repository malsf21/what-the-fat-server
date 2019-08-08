import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

usageMessage = {'usage': 'usage is incorrect! please use a POST request with a key called "answer"!'}

q1_parser = reqparse.RequestParser()
q1_parser.add_argument('answer')

class Question1(Resource):
    def get(self):
        return usageMessage
    def post(self):
        args = q1_parser.parse_args()
        if (args['answer']):
            if args['answer'] == "42":
                return {'response': 'congrats, you got the right answer! your next clue is at...'}
            else:
                return {'response': 'nice try, but that wasn\'t quite right. keep on thinking!!!'}
        else:
            return usageMessage

api.add_resource(Question1, '/switch')

if __name__ == '__main__':
    app.run(debug=True)