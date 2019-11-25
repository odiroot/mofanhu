import logging

from flask import Flask

from project.extensions import db, migrate
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


def attach_blueprints(app):
    app.register_blueprint(vanilla_bp, url_prefix="")


def register_debug(app):
    from flask_debugtoolbar import DebugToolbarExtension

    DebugToolbarExtension().init_app(app)
