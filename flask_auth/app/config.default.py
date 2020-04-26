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
    ...


class Development(Config):
    ...


class Test(Config):
    ...
