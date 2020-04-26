import os
import unittest
from app.tests.users.UserResourceTest import UserResourceTest

os.environ["APPLICATION_ENV"] = "Test"

if __name__ == "__main__":
    unittest.main()
