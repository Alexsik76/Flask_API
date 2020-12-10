from flask import jsonify, make_response, current_app
from dicttoxml import dicttoxml
from flask_restful import Resource, reqparse


class ApiReport(Resource):
    def get(self):
        data = current_app.extensions.get('table').report
        if self.get_argument().lower() == 'xml':
            response = make_response(dicttoxml(data))
            response.mimetype = "application/xml"
        else:
            response = make_response(jsonify(data))
        return response

    @staticmethod
    def get_argument():
        parser = reqparse.RequestParser()
        parser.add_argument('format')
        arg = parser.parse_args()
        return getattr(arg, 'format', 'json') or 'json'
