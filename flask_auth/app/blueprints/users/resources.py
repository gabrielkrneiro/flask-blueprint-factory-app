from pprint import pprint
from flask import jsonify, request
from flask_marshmallow.sqla import ValidationError
from flask_restful import Resource, abort

from flask_auth.app.extensions.database.database_framework import db

from flask_auth.app.blueprints.users.models import UserModel
from flask_auth.app.blueprints.users.schemas import (
    UserListSchema,
    UserCreateSchema,
    UserDetailsSchema,
    UserUpdateSchema,
)

from flask_auth.app.common.loaders import get_swagger_file_path
from flasgger import swag_from


class UserCreateListResource(Resource):
    __module__ = "users"
    user_schema = UserListSchema()
    users_schema = UserListSchema(many=True)
    user_create_schema = UserCreateSchema()
    user_model = UserModel()

    @swag_from(get_swagger_file_path(__name__, "list.yml"))
    def get(self):
        user_list = self.users_schema.dump(self.user_model.query.all())
        if not user_list:
            return abort(401, message="There is no user registered")
        return user_list

    @swag_from(get_swagger_file_path(__name__, "create.yml"))
    def post(self):
        try:
            user = self.user_create_schema.load(request.json)
            db.session.add(user)
            db.session.commit()
            db.session.close()
            return jsonify(message="User created successfully")
        except ValidationError as error:
            pprint(error.messages)
            return abort(401)


class UserDetailUpdateRemoveResource(Resource):
    user_details_schema = UserDetailsSchema()
    user_update_schema = UserUpdateSchema()
    user_model = UserModel()

    @swag_from(get_swagger_file_path(__name__, "read.yml"))
    def get(self, _id: int):
        user = self.user_details_schema.dump(
            self.user_model.query.filter_by(id=_id).first()
        )
        if not user:
            return abort(401, message="User not found")
        return user

    # TODO: Improve this update approach
    @swag_from(get_swagger_file_path(__name__, "update.yml"))
    def put(self, _id: int):
        try:
            db_user = self.user_model.query.filter_by(id=_id).first()
            if not db_user:
                return abort(401, message="User not found")
            new_user_values = self.user_update_schema.load(request.json)
            db_user.login = new_user_values.login
            db.session.commit()
            db.session.close()
            return jsonify(message="User updated successfully")
        except ValidationError as error:
            pprint(error.messages)
            return abort(401)

    @swag_from(get_swagger_file_path(__name__, "delete.yml"))
    def delete(self, _id: int):
        try:
            user = self.user_model.query.filter_by(id=_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                db.session.close()
                return jsonify(message="User removed successfully")
            return abort(401, message="User not found")
        except ValidationError as error:
            pprint(error.messages)
            return abort(
                401,
                message="Some information is lacking or invalid. Please check them and try it again.",
            )
