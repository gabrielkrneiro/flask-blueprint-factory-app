import os
from flask import Flask, jsonify

from flask_auth.app.common.logger import Logger

import flask_auth.app.extensions.restful.rest_framework as rest_framework
import flask_auth.app.extensions.database.database_framework as database_framework
import flask_auth.app.extensions.migrate.migrate_framework as migrate_framework
import flask_auth.app.extensions.serializer.serializer_framework as serializer_framework

import flask_auth.app.blueprints.users as user_module


logger = Logger(__file__).getLogger()


def minimal_app(**config):
    app = Flask(__name__)
    app.secret_key = "S0M3S3CR3TK3Y"
    app.config.from_object(
        "flask_auth.app.config." + os.getenv("APPLICATION_ENV", "Development")
    )
    return app


def main_app(**config):
    # Extensions
    app = minimal_app()

    @app.route("/")
    def index_route():
        return jsonify(message="Server is running...")

    database_framework.init_app(app)
    logger.info("Finish to initialize extension: Database")
    rest_framework.init_app(app)
    logger.info("Finish to initialize extension: REST Api")
    migrate_framework.init_app(app)
    logger.info("Finish to initialize extension: Migrate")
    serializer_framework.init_app(app)
    logger.info("Finish to initialize extension: Serializer")

    # Blueprints
    user_module.init_app(app)
    logger.info("Finish to initialize blueprint: Users")

    return app
