from flask import Flask
from flasgger import Swagger

swagger = Swagger()


def init_app(app: Flask):
    swagger.init_app(app)
