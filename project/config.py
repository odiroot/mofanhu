import os

from environs import Env


# Load environment variables.
env = Env()

# Paths.
HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)

# General Flask settings.
ENV = env.str("FLASK_ENV", "production")
DEBUG = ENV == "development"
LOG_LEVEL = env.log_level("LOG_LEVEL", "INFO")
SECRET_KEY = env.str("SECRET_KEY")

# DB access / ORM.
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# API spec/docs hosting.
API_TITLE = 'Flask Application Template'
API_VERSION = 'v1'
OPENAPI_VERSION = '3.0.2'
OPENAPI_URL_PREFIX = "/smorest"
OPENAPI_SWAGGER_UI_PATH = "/docs"
OPENAPI_SWAGGER_UI_VERSION = "3.24.2"

# Background tasks.
DRAMATIQ_BROKER_URL = env.str("BROKER_URL", "redis://localhost:6379/3")

# Debug toolbar.
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Admin pages.
FLASK_ADMIN_SWATCH = "sandstone"
