from flask import Flask
from flask_restful import Resource, Api
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Mi API', description='Descripción de mi API')

# @api.route('/hello')
# class Hello(Resource):
#     def get(self):
#         """Saluda al usuario"""
#         return {'message': '¡Hola, mundo!'}

if __name__ == '__main__':
    app.run(debug=True)
