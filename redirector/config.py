# coding=utf-8
"""
config module
"""

NAMESPACE = 'REDIRECTOR_'

class Config(object):
    REDIRECTOR_SCHEME = 'https'
    REDIRECTOR_HOST = 'www.example.com'
    REDIRECTOR_BASE_PATH = '/' # Note: Base path must always end with a '/'
    REDIRECTOR_PORT = 443
    REDIRECTOR_REDIRECT_CODE = 301
