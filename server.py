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

q2_parser = reqparse.RequestParser()
q2_parser.add_argument('answer')
q2_parser.add_argument('questionID')

class Question1(Resource):
    def get(self):
        return usageMessage
    def post(self):
        args = q1_parser.parse_args()
        if (args['answer']):
            if args['answer'] == "42":
                return {'response': 'congrats, you got the right answer! your next clue is <a href="https://whatthefatdog.com/mastering-physics/">here</a>'}
            else:
                return {'response': 'nice try, but that wasn\'t quite right. keep on thinking!!!'}
        else:
            return usageMessage
            
class Question2(Resource):
    def get(self):
        return usageMessage
    def post(self):
        args = q2_parser.parse_args()
        if (args['answer'] and args['questionID']):
            if args['questionID'] == 'a' and args['answer'] == '1.528':
                return {
                    'correct': True,
                    'response': 'nice, that\'s correct!',
                    'question': '''
                    <p>
                    Good job. Now forget that answer since you don’t really need it. 
                    </p>
                    <p>
                    Huan rides his sKateboard from T Plate to class while eating his breakfast burrito, at a Speed of 150322 furlong/fortnight. One day when he’s not paying attention, bc his bUrrito is too FAT, he collided with another skater, Tania Raya of Mass 1768.29 troy ounces. She juMps on and they both now ride the same skateboard to class. 
                    </p>
                    <img src="img/burrito.png" alt="phat burrrrrrrrito" />
                    <p>
                    (b) At whAt new speed are they moving at? Enter answeR in m/s.</p>''',
                    'questionID': 'b'
                }
            elif args['questionID'] == 'b' and args['answer'] == '13.04':
                return {
                    'correct': True,
                    'response': '''
                        <p>
                        Realising that they’ll both be late for class at thIs speed, Huan quickly finds a nEw solution. 
                        </p>
                        <img src="img/sdmv.png" alt="look at that EFFICIENCY" />
                        <p>
                        He finds a Super Duper Mileage Vehicle parked and they both hop on. The car saveS them and they reach at 1:00PM, just in time for Physics class.
                        </p>
                        <p>
                        That's it for this riddle! Now, it's up to YOU to find the next one 🤔
                        </p>
                    ''',
                    'question': '',
                    'questionID': 'c'
            }
            else:
                return {'correct': False,'response': 'nice try, but that wasn\'t quite right. keep on thinking!!!'}
        else:
            return usageMessage

api.add_resource(Question1, '/switch')
api.add_resource(Question2, '/mastering-physics')

if __name__ == '__main__':
    app.run(debug=True)