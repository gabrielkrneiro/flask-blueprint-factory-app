import os

from flask import Flask

import flask_auth.extensions.restful.rest_framework as rest_framework
import flask_auth.extensions.database.database_framework as database_framework
import flask_auth.extensions.migrate.migrate_framework as migrate_framework
import flask_auth.extensions.serializer.serializer_framework as serializer_framework

import flask_auth.blueprints.users as user_module


app = Flask(__name__)
app.secret_key = 'S0M3S3CR3TK3Y'
app.config.from_object('flask_auth.config.' + os.getenv('APPLICATION_ENV', 'Development'))

# Extensions
database_framework.init_app(app)
rest_framework.init_app(app)
migrate_framework.init_app(app)
serializer_framework.init_app(app)

# Blueprints
user_module.init_app(app)

