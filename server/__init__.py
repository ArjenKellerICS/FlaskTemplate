# imports
import os
from flask import Flask
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

    return server
