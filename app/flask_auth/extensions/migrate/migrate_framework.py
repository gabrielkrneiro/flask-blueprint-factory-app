from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.flask_auth.extensions.database.database_framework import db


def init_app(app: Flask):
    migrate = Migrate(app, db)
    return migrate
