from flask_restful import Resource, fields, marshal_with
from flask_restful.reqparse import RequestParser

from project.extensions import db
from project.vanilla.models import Example


class Index(Resource):
    def get(self):
        return dict(message="Hello world")


class ExampleList(Resource):
    # Output format.
    example_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "good": fields.Boolean,
    }
    # Input format.
    parser = RequestParser(trim=True, bundle_errors=True)
    parser.add_argument("name", required=True, location="json")
    parser.add_argument("good", type=bool, location="json")

    @marshal_with(example_fields)
    def get(self):
        return Example.query.all()

    @marshal_with(example_fields)
    def post(self):
        args = self.parser.parse_args()

        obj = Example(**args)
        db.session.add(obj)
        db.session.commit()

        return obj, 201
