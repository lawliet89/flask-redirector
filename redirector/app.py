# coding=utf-8
""" redirector app factory

"""

from flask import Flask
from .views import blueprint
from . import config
import os


def create_app(**kwargs):
    """Create a flask app"""
    app = Flask(__name__)
    settings = config.make_settings()

    app.config.update({ key: value.default for key, value in settings.items() })

    config_file = kwargs.get('CONFIG_FILE')
    if config_file is not None:
        app.config.from_pyfile(config_file)

    known_settings = [setting.name.upper() for _, setting in settings.items()]
    override_mappings = { (config.NAMESPACE + key) : value for key, value in kwargs.items()
                          if value is not None and key in known_settings }
    app.config.update(override_mappings)

    app.register_blueprint(blueprint)

    return app
