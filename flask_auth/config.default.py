import os


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    # dont remove ENV attribute
    ...


class DevelopmentConfig(Config):
    # dont remove ENV attribute
    ...


class TestingConfig(Config):
    # dont remove ENV attribute
    ...
