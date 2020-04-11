import unittest
import socket
import requests
import os
import json

from flask import Flask, url_for

from flask_auth.blueprints.users.schemas import UserDetailsSchema, UserListSchema
from flask_auth.blueprints.users.models import UserModel
from flask_auth.blueprints.users.resources import UserCreateListResource
from tests import client, db

"""
TODO: Necessary configure setUp() and tearDown() correctly due database connection.
TODO: Configure mocked data to test environment
"""


class UserResourceTest(unittest.TestCase):
    def setUp(self):
        ...

    def tearDown(self):
        ...

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
