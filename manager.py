#!/usr/bin/env python3
# coding=utf-8
""" service manager script

"""
import os
import sys
from flask import current_app
from flask_script import Manager, Command, Option
from gunicorn.app.base import BaseApplication
from gunicorn.config import make_settings
from redirector import create_app

manager = Manager(create_app)  # pylint: disable=invalid-name

manager.add_option('-c', '--config-file', dest='CONFIG_FILE', required=False,
    help="Provide a path to an ini file for configuration")
manager.add_option('--scheme', dest='SCHEME', required=False, choices=['http', 'https'],
    help="The scheme to redirect users to")
manager.add_option('--host', dest='HOST', required=False,
    help="The HTTP Host to redirect users to")
manager.add_option('--base-path', dest='BASE_PATH', required=False,
    help="The base path to redirect users to")
manager.add_option('--port', dest='PORT', required=False, type=int,
    help="The port to redirect users to")
manager.add_option('--redirect-code', dest='REDIRECT_CODE', required=False, type=int,
    help="The HTTP redirect code for use in redirecting")

class GunicornApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def get_options(self): # Pretty crude way of mapping gunicorn options. Might have to fix
        settings = make_settings()
        options = (
            Option(*klass.cli)
            for setting, klass in settings.items() if klass.cli
        )
        return options

    def run(self, *args, **kwargs):
        GunicornApplication(current_app, kwargs).run()

manager.add_command('gunicorn', GunicornServer())

if __name__ == "__main__":
    manager.run()
