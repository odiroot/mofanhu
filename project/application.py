import logging

from flask import Flask

from project.extensions import api, broker, db, migrate
from project.restful import bp as restful_bp
from project.smorest.views import bp as smorest_bp
from project.vanilla.views import bp as vanilla_bp


log = logging.getLogger(__name__)


def create_app(config_module="project.config"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_module)

    configure_logging(app)
    register_extensions(app)
    attach_blueprints(app)

    if app.config["DEBUG"]:
        register_debug(app)

    return app


def configure_logging(app):
    logging.basicConfig(level=app.config["LOG_LEVEL"])


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    broker.init_app(app)


def attach_blueprints(app):
    app.register_blueprint(vanilla_bp, url_prefix="")
    app.register_blueprint(restful_bp, url_prefix="/restful")
    api.register_blueprint(smorest_bp, url_prefix="/smorest")


def register_debug(app):
    from flask_debugtoolbar import DebugToolbarExtension

    DebugToolbarExtension().init_app(app)
