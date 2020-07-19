import pytest
import sqlalchemy as sa
from environs import Env

from project.application import create_app
from project.extensions import db


env = Env()
pytest_plugins = ["pytest-flask-sqlalchemy"]


class Config:
    DEBUG = False
    LOG_LEVEL = "ERROR"
    TESTING = True
    SECRET_KEY = "testing"
    SQLALCHEMY_DATABASE_URI = env.str("TEST_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture(scope="session")
def database(request, worker_id):
    url = sa.engine.url.make_url(Config.SQLALCHEMY_DATABASE_URI)
    # Template for worker-specific databases.
    base_name = url.database
    # Connect without a specific DB.
    url.database = None
    # Avoid problems with transactions.
    engine = sa.create_engine(url, isolation_level="AUTOCOMMIT")

    database = f"{base_name}_{worker_id}"

    # Create test database.
    engine.execute("ROLLBACK")
    engine.execute(f"CREATE DATABASE {database}")

    @request.addfinalizer
    def drop_db():
        # Drop test database.
        engine.execute("ROLLBACK")
        engine.execute(f"DROP DATABASE {database}")


@pytest.fixture(scope="session")
def app(database):
    app = create_app(Config)
    app.test_request_context().push()
    return app


@pytest.fixture(scope="session")
def _db(request, app):
    db.create_all()
    return db
