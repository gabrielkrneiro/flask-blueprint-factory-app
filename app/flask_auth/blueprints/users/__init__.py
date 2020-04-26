from flask import Blueprint, Flask
from flask_restful import Api

from .resources import UserCreateListResource, UserDetailUpdateRemoveResource

bp = Blueprint("users", __name__, url_prefix="/api/users")
api = Api(bp)


def init_app(app: Flask):
    api.add_resource(UserCreateListResource, "/")
    api.add_resource(UserDetailUpdateRemoveResource, "/<int:_id>")
    app.register_blueprint(bp)
