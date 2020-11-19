import dramatiq
from flask_admin import Admin
from flask_melodramatiq import RedisBroker
from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
api = Api(spec_kwargs=dict(openapi_version="3.0.2", host="localhost:5000"))
broker = RedisBroker()
dramatiq.set_broker(RedisBroker)
admin = Admin(name="Management", template_mode="bootstrap3")
