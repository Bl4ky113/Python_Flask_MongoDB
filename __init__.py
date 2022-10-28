
from flask import Flask
from . import config

def create_app (test_config=False):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.Config)

    return app
