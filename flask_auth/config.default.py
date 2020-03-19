import os


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    # dont remove ENV attribute
    ENV = __qualname__


class DevelopmentConfig(Config):
    # dont remove ENV attribute
    ENV = __qualname__


class TestingConfig(Config):
    # dont remove ENV attribute
    ENV = __qualname__
