from flask import jsonify, request
from flask_restful import Resource, abort
from .models import UserModel, UserListSchema
from flask_auth.extensions.database.database_framework import db


class UserCreateListResource(Resource):

    user_schema = UserListSchema()
    users_schema = UserListSchema(many=True)

    def get(self):
        return self.users_schema.dump(UserModel.query.all())

    @staticmethod
    def post():
        login = request.json['login']
        password = request.json['password']
        user = UserModel(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return jsonify(message='User created successfully')
