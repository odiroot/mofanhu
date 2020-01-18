from flask.blueprints import Blueprint
from flask_restful import Api

from .resources import ExampleList, Index


bp = Blueprint("restful", __name__)
api = Api(bp)

api.add_resource(Index, "/")
api.add_resource(ExampleList, "/example/")
