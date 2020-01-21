import os

from environs import Env


env = Env()

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)


ENV = env.str("FLASK_ENV", "production")
DEBUG = ENV == "development"
LOG_LEVEL = env.log_level("LOG_LEVEL", "INFO")
SECRET_KEY = env.str("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

OPENAPI_URL_PREFIX = "/smorest"
OPENAPI_SWAGGER_UI_PATH = "/docs"
OPENAPI_SWAGGER_UI_VERSION = "3.24.2"
