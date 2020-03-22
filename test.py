import os
import unittest
from flask_auth.app import minimal_app
from flask_auth.tests.users.UserResourceTest import UserResourceTest

os.environ['APPLICATION_ENV'] = 'Test'

if __name__ == '__main__':
    unittest.main()
