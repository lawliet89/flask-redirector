# coding=utf-8
""" views module

"""
from urllib.parse import urlunparse, urljoin
from flask import Blueprint, request, current_app, redirect
from .config import NAMESPACE

blueprint = Blueprint(  # pylint: disable=invalid-name
    'redirector',
    __name__
)


@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def all_paths(path):
    full_path = request.full_path
    config = get_config()
    redirect_url = make_redirect_url(full_path, config['scheme'], config['host'], config['port'], config['base_path'])
    return redirect(redirect_url, int(config['redirect_code']))


def get_config():
    return current_app.config.get_namespace(NAMESPACE)


def make_redirect_url(path, scheme, host, port, base_path):
    base_url = make_base_url(scheme, host, port, base_path)
    return urljoin(base_url, path)


def normalize_port(scheme, port):
    port = int(port)
    if scheme == 'http' and port == 80:
        return None
    elif scheme == 'https' and port == 443:
        return None
    return port


def make_base_url(scheme, host, port, base_path):
    normalized_port = normalize_port(scheme, port)
    host_with_port = ":".join(filter(None, [host, str(normalized_port)]))
    unparsed_tuples = (scheme, host_with_port, base_path, '', '', '')
    return urlunparse(unparsed_tuples)
