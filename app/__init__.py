import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='1231231231231ijisfisdjfs',
        DEBUG = True,
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:tuhanku4JJ@localhost/postapps_db',
        SQLALCHEMY_TRACK_MODIFICATIONS = True,
        SQLALCHEMY_ECHO = True
    )

    from .extensions._db import db, setup_db
    setup_db(app)

    @app.route('/')
    def index():
        return 'Home'

    return app
