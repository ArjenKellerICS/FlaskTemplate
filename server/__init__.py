# imports
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy object
db = SQLAlchemy()


# Application factory
def create_server():
    from .config import config_by_name
    from .server_extensions import initialize_extensions
    from .server_routes import register_routes

    # initialize flask wsgi instance
    server = Flask(__name__)

    # apply the configs from server.config.py through environment variables
    server.config.from_object(config_by_name[os.environ.get("ENVIRONMENT") or 'dev'])

    # initialize the applied flask extensions
    initialize_extensions(server)

    # register all routing from other modules
    register_routes(server)

    @server.route("/deploy-db/<secret_key>")
    def deploy_db(secret_key):
        if secret_key == server.config["SECRET_KEY"]:
            db.create_all()
            return jsonify(True)
        else:
            return jsonify(False)

    return server
