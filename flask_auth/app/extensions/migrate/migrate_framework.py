from flask import Flask

from flask_migrate import Migrate
from flask_auth.app.extensions.database.database_framework import db


def init_app(app: Flask):
    migrate = Migrate(app, db)
    return migrate
