from flask import Flask
from flasgger import Swagger

swagger = Swagger()


def init_app(app: Flask):
    app.config["SWAGGER"] = {
        "title": "Flask Auth",
        "version": "1.0.0",
        "description": "Open Source project to demonstrate Factory App + Blueprints pattern usage in Python projects",
        "license": "MIT",
        "termsOfService": "https://github.com/GabrielCarneiroDeveloper/flask-blueprint-factory-app",
    }
    swagger.init_app(app)
