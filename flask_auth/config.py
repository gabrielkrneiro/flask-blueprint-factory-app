import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data.db'
    API_VERSION = 'v1'


class Production(Config):
    HOST = '0.0.0.0'
    DATABASE_URI = 'mysql://user@localhost/foo'
    PORT = '5010'
    SECRET_KEY = 'secret_key_prod'
    ENV = __qualname__


class Development(Config):
    HOST = 'localhost'
    DEBUG = True
    PORT = '5000'
    SECRET_KEY = 'secret_key_dev'
    ENV = __qualname__


class Test(Config):
    HOST = '0.0.0.0'
    TESTING = True
    PORT = '3214'
    SECRET_KEY = 'secret_key_test'
    ENV = __qualname__
