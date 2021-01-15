from flask import jsonify, make_response
from dicttoxml import dicttoxml
from flask_restful import Resource, reqparse
from playhouse.shortcuts import model_to_dict
from app.models import Racer


class ApiReport(Resource):
    def get(self):
        """
        file: ./docs/spec.yml
        """

        data = [model_to_dict(racer) for racer in Racer.select().order_by(Racer.id)]
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
