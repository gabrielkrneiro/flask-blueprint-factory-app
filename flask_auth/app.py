import sqlite3
import os

from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, abort, Resource
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
from flask_auth.config import DevelopmentConfig, ProductionConfig, TestingConfig

load_dotenv()

app = Flask(__name__)

app.config.from_object('flask_auth.config.DevelopmentConfig')

api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

PREFIX = '/api'
API_VERSION = "/" + app.config['API_VERSION']  # /v1, /v2,...
BASE_URL = PREFIX + API_VERSION


class HomeResource(Resource):
    base_endpoint = '/'

    def get(self):
        return jsonify(status='Running',
                       port=int(app.config['PORT']),
                       version=app.config['API_VERSION'],
                       modules=[{
                           'users': {
                               'href': UserResource.base_endpoint
                           }
                       }])


class UserResource(Resource):
    base_endpoint = BASE_URL + '/users'

    def get(self):
        return 'list'


##############################
# Shell Context
##############################
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)


##############################
# Routes
##############################

api.add_resource(HomeResource, HomeResource.base_endpoint)
api.add_resource(UserResource, UserResource.base_endpoint)
