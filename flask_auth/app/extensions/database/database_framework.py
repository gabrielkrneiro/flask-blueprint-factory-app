from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.config["DATABASE_CONNECTION"] = db
