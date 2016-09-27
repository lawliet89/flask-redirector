# coding=utf-8
"""
config module -- adapted from gunicorn
"""

NAMESPACE = 'REDIRECTOR_'


class Setting(object):
    name = None
    cli = None
    choices = None
    default = None
    help = None
    type = str
    required = False


class Scheme(Setting):
    name = 'scheme'
    cli = ['--scheme']
    choices = ['http', 'https']
    default = 'https'
    help = 'The scheme to redirect users to'


class Host(Setting):
    name = 'host'
    cli = ['--host']
    default = 'www.example.com'
    help = 'The HTTP Host to redirect users to'


class BasePath(Setting):
    name = 'base_path'
    cli = ['--base-path']
    default = '/'
    help = 'The base path to redirect to. Must end in "/"'


class Port(Setting):
    name = 'port'
    cli = ['--port']
    default = 443
    help = 'The port number to redirect to'
    type = int


class RedirectCode(Setting):
    name = 'redirect_code'
    cli = ['--redirect-code']
    default = 301
    help = 'The HTTP status code for use in redirecting'
    type = int


class ConfigFile(Setting):
    name = 'config_file'
    cli = ['-c', '--config-file']
    help = 'Provide a path to an ini file for configuration'


KNOWN_SETTING = [Scheme, Host, BasePath, Port, RedirectCode, ConfigFile]

def make_settings():
    return { NAMESPACE + setting.name.upper(): setting  for setting in KNOWN_SETTING }
