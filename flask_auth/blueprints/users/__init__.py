from flask import Blueprint, Flask
from .resources import UserCreateListResource
from flask_restful import Api

bp = Blueprint('users', __name__)
api = Api(bp)


def init_app(app: Flask):
    api.add_resource(UserCreateListResource, "/")
    app.register_blueprint(bp)

