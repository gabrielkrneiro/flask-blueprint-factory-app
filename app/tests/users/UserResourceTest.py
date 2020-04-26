import unittest
import json

from flask import Flask, url_for

from app.flask_auth.blueprints.users.models import UserModel
from app.flask_auth.blueprints.users.resources import UserCreateListResource
from app.tests import client

from app.tests.users.UserModelMockFactory import UserModelMockFactory
from app.tests.users.UserModelMock import UserModelMock

"""
TODO: Necessary configure setUp() and tearDown() correctly due database connection.
TODO: Configure mocked data to test environment
"""


class UserResourceTest(unittest.TestCase):
    def setUp(self):
        self.users = UserModelMockFactory(number_of_users=2)
        self.users.save_mocks_in_database()

    def tearDown(self):
        self.users.remove_all_registers_from_database()

    def test_should_return_200_if_server_is_running(self):
        response = client.get(path=url_for("index_route"))
        self.assertEqual(response.status_code, 200)

    def test_should_get_user_list(self):
        response = client.get(path=url_for("users.usercreatelistresource"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_should_get_user_details(self):
        first_user = UserModel().query.all()[0]
        response = client.get(
            path=url_for("users.userdetailupdateremoveresource", _id=first_user.id)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["login"])
        self.assertIsNotNone(response.json["password"])
        self.assertIsNotNone(response.json["id"])

    def test_should_get_an_user_created_successfully(self):
        response = client.post(
            path=url_for("users.usercreatelistresource"),
            data=json.dumps({"login": "gabu", "password": "senha123"}),
            follow_redirects=True,
            mimetype="application/json",
        )
        self.assertEqual(200, response.status_code)

    def test_should_get_an_user_removed_successfully(self):
        first_user = UserModel().query.all()[0]
        response = client.delete(
            path=url_for("users.userdetailupdateremoveresource", _id=first_user.id),
            follow_redirects=True,
            mimetype="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_should_get_login_user_updated_with_new_login_successfully(self):
        first_user = UserModel().query.all()[0]
        new_login = "ANOTHER_NAME"
        response = client.put(
            path=url_for("users.userdetailupdateremoveresource", _id=first_user.id),
            data=json.dumps({"login": new_login}),
            follow_redirects=True,
            mimetype="application/json",
        )
        updated_user = UserModel().query.all()[0]
        self.assertEqual(new_login, updated_user.login)
