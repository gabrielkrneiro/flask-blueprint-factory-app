import unittest
import socket
import requests
import os

from flask import Flask

from flask_auth.blueprints.users.schemas import UserDetailsSchema
from flask_auth.app import minimal_app, main_app


class UserResourceTest(unittest.TestCase):

    api_address: str
    app = main_app()
    client = app.test_client()

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_should_return_200_if_server_is_running(self):
        response = self.client.get(path='/', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_should_get_user_list(self):
        response = self.client.get(path='/api/users', follow_redirects=False)
        self.assertEqual(response.status_code, 308)

    def test_should_get_user_details(self):
        response = self.client.get(path='/api/users/2')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['login'])
        self.assertIsNotNone(response.json['password'])
        self.assertIsNotNone(response.json['id'])

    def test_should_get_an_user_created_successfully(self):
        ...

    def test_should_get_an_user_removed_successfully(self):
        ...

    def test_should_return_200_if_user_is_removed_successfully(self):
        ...

    def test_should_get_an_user_updated_successfully(self):
        ...