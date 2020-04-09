from flask_auth.app import minimal_app, main_app
import tempfile
from flask import jsonify
import sqlite3
import os

"""
TODO: Configure test database name with app.config 
TODO: Avoid have to use schema.sql in database_dev.db creation
"""

app = main_app()
app.testing = True
app_context = app.test_request_context()
app_context.push()

db_fd, app.config["DATABASE"] = tempfile.mkstemp()
app.config["TESTING"] = True

client = app.test_client()

with app.app_context():
    db = sqlite3.connect("data_test.db", detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row

    with app.open_resource("../schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


# @app.shell_context_processor
# def shell_context(**kwargs):
#     return dict(app=app, db=db)
