import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data.db'
    API_VERSION = 'v1'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    PORT = '5010'
    SECRET_KEY = 'secret_key_prod'


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = '5000'
    ENV = 'development'
    SECRET_KEY = 'secret_key_dev'


class TestingConfig(Config):
    TESTING = True
    PORT = '3214'
    SECRET_KEY = 'secret_key_test'
