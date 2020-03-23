#!/usr/bin/env python
# coding: utf-8

from flask import Flask, g
from utils4py.flask_utils import CustomJSONEncoder
from flask_cors import CORS
from .common import db, cache
from .error.error_handler import error_response

app = Flask(
    __name__, instance_relative_config=True, static_folder="public", static_url_path=""
)

app.config.from_object("config")
app.config.from_pyfile("db.py", silent=True)
app.config.from_pyfile("redis.py", silent=True)
app.config.from_pyfile("app.py", silent=True)

if app.config["CORS_ENABLED"]:
    CORS(app)

app.json_encoder = CustomJSONEncoder

from . import middleware


@app.errorhandler(Exception)
def error_handler(error):
    g._error = error
    if error:
        db.session.rollback()

    return error_response(error)


@app.teardown_request
def teardown_request(error):
    try:
        if not hasattr(g, "_error") or not g._error:
            db.session.commit()
    finally:
        db.session.close()


def init_app():
    """
    initialize app
    """
    cache.init_app(app)
    db.init_app(app)


def create_app():
    init_app()

    from .views import routes

    app.register_blueprint(routes)

    return app
