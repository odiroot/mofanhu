from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
api = Api(spec_kwargs=dict(
    openapi_version="3.0.2",
    host="localhost:5000",
))
