from flask_auth.app import minimal_app, main_app
import tempfile
from flask import jsonify
import sqlite3
import os
from flask_auth.extensions.database.database_framework import db

"""
TODO: Configure test database name with app.config 
TODO: Avoid have to use schema.sql in database_dev.db creation
"""
os.environ["APPLICATION_ENV"] = "Test"

app = main_app()
app.testing = True
app_context = app.test_request_context()
app_context.push()
client = app.test_client()
