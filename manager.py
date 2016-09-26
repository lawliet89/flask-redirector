#!/usr/bin/env python3
# coding=utf-8
""" service manager script

"""
from flask_script import Manager
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


if __name__ == "__main__":
    manager.run()
