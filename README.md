# mofanhu
A robust template for Flask applications.

![https://www.flickr.com/photos/sophies/5393505900/](./project/static/flask.jpg)

> [..] Put water into a bottle it becomes the bottle.

## Features

- Python 3.8 as a base.
- Clean and organised structure for a medium size or large web project.
- Staying close to the _12 Factor App_ ideals.
- Well configured Flask CLI tool for user friendliness.
- Integrated _Konch_ and _DebugToolbar_ for easier debugging.
- Project configuration based on _environs_ for automatic validation and
  type conversion.
- Development configuration using _direnv_, overridable by environment
  variables.
- Serving dynamically rendered HTML page and example static files with pure
  Flask. Example template.
- Example API endpoints in two flavours: _Flask-RESTful_ and _flask-smorest_.
- Support for _PostgreSQL_ database and ORM models using _SQLAlchemy_.
  Example model.
- Support for migrations with _alembic_. Example migration.
- Support for background tasks with _dramatiq_. Example task.
- Configuration for running on _Heroku_ cloud.
- Separate production, testing and development requirements.
- Easy testing with _tox_ and _py.test_. Example tests.
- Support for fast and efficient testing of database code using transactions and
  parallel workers.
- Basic code linting with _black_, _flake8_ and _isort_.
- Github Actions testing with _Python application_ setup.
- Easy entry vector for WSGI servers, demonstrated with _Gunicorn_.
- _Dockerfile_ to build a minimal¸ production-ready Docker image.
- Rudimentary definition for _Docker Compose_ to launch the complete project.
- Practical CRUD UI using Flask-Admin.
- _EditorConfig_ support.

## Running

### With Docker

*Note*: Ensure you have a working system Docker installation.

Install Docker Compose:

    $ pip install -U docker-compose

Start the complete stack in a standard way:

    $ docker-compose up --build --detach

Check the logs

    $ docker-compose logs --follow

### Manually

*Note*: Ensure you have a working Python 3.8 installation.

Create a virtualenv:

    $ virtualenv -p `which python3.8` .env

Install dependencies:

    $ source .env/bin/activate
    $ pip install -Ur requirements.txt

Prepare the environment (_direnv_ has to be preinstalled):

    $ cp envrc.example .envrc
    $ direnv edit

Run the development web server:

    $ flask run

### Tests

Install the tooling:

    $ pip install -U tox

Run the tests

    $ tox
