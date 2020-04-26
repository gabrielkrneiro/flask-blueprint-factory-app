import os
from abc import ABC


class Config(ABC):
    DEBUG: bool
    TESTING: bool
    DATABASE_URI: str
    ENV: str
    HOST: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
    SQLALCHEMY_DATABASE_URI: str
    API_VERSION: str
    PORT: str
    SECRET_KEY: str


class Production(Config):
    ENV = "Production"
    HOST = "0.0.0.0"
    PORT = "5010"
    DATABASE_URI = "mysql://user@localhost/foo"
    SECRET_KEY = "secret_key_prod"
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data.db'
    API_VERSION = "v1"


class Development(Config):
    ENV = "Development"
    HOST = "0.0.0.0"
    PORT = "5000"
    DEBUG = True
    SECRET_KEY = "secret_key_dev"
    TESTING = False
    DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data.db'
    API_VERSION = "v1"


class Test(Config):
    ENV = "Test"
    HOST = "0.0.0.0"
    PORT = "3214"
    DEBUG = True
    TESTING = True
    SECRET_KEY = "secret_key_test"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data_test.db'
    DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_VERSION = "v1"
    SECRET_KEY = "TestingSecretKey"
