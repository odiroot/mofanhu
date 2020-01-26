"""Entry vector for Dramatiq workers."""
from project.application import create_app
from project.extensions import broker  # noqa
from project.tasks import example_task  # noqa


app = create_app()
