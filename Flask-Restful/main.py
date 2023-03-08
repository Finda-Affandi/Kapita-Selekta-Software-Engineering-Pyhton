from flask import Flask, jsonify, request, Response, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return make_response(jsonify({'hello': 'world'}), 200)

    def post(self):
        data = request.get_json()
        strAlpha = f"{data['nama']} berasald dari {data['asal']}"
        return strAlpha

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)