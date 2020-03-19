from flask_auth.extensions.database.database_framework import db

from flask_auth.extensions.serializer.serializer_framework import ma


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


class UserListSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        fields = ('login',)
