from flask.views import MethodView
from flask_smorest import Blueprint

from project.extensions import db
from project.smorest.schemas import ExampleSchema
from project.vanilla.models import Example


bp = Blueprint("smorest", __name__, description="Flask-smorest examples")


@bp.route("/")
class Index(MethodView):
    def get(self):
        """Greeting message.

        Be nice and say hello.
        """
        return dict(message="Hello world")


@bp.route("/example/")
class ExampleList(MethodView):
    @bp.response(ExampleSchema(many=True))
    def get(self):
        """List examples.

        Retrieve all examples from the DB.
        """
        return Example.query.all()

    @bp.arguments(ExampleSchema)
    @bp.response(ExampleSchema, code=201)
    def post(self, data):
        """Create an example.

        Add a new example to the DB.
        """
        obj = Example(**data)
        db.session.add(obj)
        db.session.commit()
        return obj
