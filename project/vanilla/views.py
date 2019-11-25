from flask import render_template
from flask.blueprints import Blueprint

from .models import Example


bp = Blueprint(
    "vanilla",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/vanilla",
)


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html", examples=Example.query.all())
