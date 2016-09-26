# coding=utf-8
""" redirector app factory

"""

from flask import Flask
from .views import blueprint
from . import config
import os

ALLOWED_MAPPINGS = ['SCHEME', 'HOST', 'BASE_PATH', 'PORT', 'REDIRECT_CODE']


def create_app(**kwargs):
    """Create a flask app"""
    app = Flask(__name__)

    app.config.from_object(config.Config)

    config_file = kwargs.get('CONFIG_FILE')
    if config_file is not None:
        app.config.from_pyfile(config_file)

    override_mappings = { (config.NAMESPACE + key) : value for key, value in kwargs.items()
                          if value is not None and key in ALLOWED_MAPPINGS }
    app.config.update(override_mappings)

    app.register_blueprint(blueprint)
    return app
