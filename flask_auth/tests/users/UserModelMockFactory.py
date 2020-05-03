from .UserModelMock import UserModelMock
from typing import List
from flask_auth.app.extensions.database.database_framework import db


class UserModelMockFactory:
    user_list: List
    user_list_copy: List
    number_of_users: int

    def __init__(self, number_of_users: int):
        """ __new__ is used instead of __init__ because have to be a list
        assigned as UserModelMockFactory instance, not an object.
        The value assigned to its instance will be the value
        returned from __new__ """
        self.user_list = []
        self.number_of_users = number_of_users
        for u in range(self.number_of_users):
            self.user_list.append(UserModelMock())

        # it keeps an user_list copy
        self.user_list_copy = self.user_list.copy()

    def save_mocks_in_database(self):
        for user in self.user_list:
            db.session.add(user)
        db.session.commit()
        db.session.close()

    def remove_all_registers_from_database(self):
        db.session.query(UserModelMock).delete()
        db.session.commit()
