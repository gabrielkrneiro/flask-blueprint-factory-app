from flask_auth.blueprints.users.models import UserModel
from faker import Faker

fake = Faker()


class UserModelMock(UserModel):
    """ Extends UserModel and loads fake data to the seeder """

    def __init__(self):
        self.login = fake.email()
        self.password = "senha123"
        super().__init__()
