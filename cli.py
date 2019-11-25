import os

from project.application import create_app
from project.extensions import db
from project.vanilla.models import Example


app = create_app()

# Konch-specific additions.
app.config.update(
    {
        "KONCH_FLASK_IMPORTS": False,  # No mass import of Flask utils.
        "KONCH_CONTEXT_FORMAT": "short",
    }
)


@app.shell_context_processor
def shell_context():
    return dict(
        db=db,
        # Directly expose known models.
        Example=Example,
    )


@app.cli.command()
def test():
    from pytest import main

    test_path = os.path.join(app.config["PROJECT_ROOT"], "tests")
    result = main([test_path])
    exit(result)
