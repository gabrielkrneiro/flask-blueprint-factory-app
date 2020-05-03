from flask_auth.app.blueprints.users.models import UserModel
from flask_auth.app.extensions.serializer.serializer_framework import ma


class UserListSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("id", "login")


class UserDetailsSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("id", "login", "password")


class UserCreateSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("login", "password")


class UserUpdateSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ("login",)
