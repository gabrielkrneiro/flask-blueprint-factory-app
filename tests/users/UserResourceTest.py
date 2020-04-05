import unittest
import socket
import requests
import os
import json

from flask import Flask, url_for

from flask_auth.blueprints.users.schemas import UserDetailsSchema, UserListSchema
from flask_auth.app import minimal_app, main_app
from flask_auth.blueprints.users.models import UserModel
from flask_auth.blueprints.users.resources import UserCreateListResource


class UserResourceTest(unittest.TestCase):

    app = main_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    client = app.test_client()

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_should_return_200_if_server_is_running(self):
        response = self.client.get(path=url_for("index_route"), follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_should_get_user_list(self):
        response = self.client.get(path=url_for("users.usercreatelistresource"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_should_get_user_details(self):
        response = self.client.get(
            path=url_for("users.userdetailupdateremoveresource", _id=2)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["login"])
        self.assertIsNotNone(response.json["password"])
        self.assertIsNotNone(response.json["id"])

    def test_should_get_an_user_created_successfully(self):
        response = self.client.post(
            path=url_for("users.usercreatelistresource"),
            data=json.dumps({"login": "gabu", "password": "senha123"}),
            follow_redirects=True,
            mimetype="application/json",  # ,
        )
        self.assertEqual(200, response.status_code)

    def test_should_get_an_user_removed_successfully(self):
        raise Exception(
            "You should implement test_should_get_an_user_removed_successfully()"
        )

    def test_should_return_200_if_user_is_removed_successfully(self):
        raise Exception(
            "You should implement test_should_return_200_if_user_is_removed_successfully()"
        )

    def test_should_get_an_user_updated_successfully(self):
        raise Exception(
            "You should implement test_should_get_an_user_updated_successfully()"
        )
