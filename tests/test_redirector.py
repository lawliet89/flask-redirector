# coding=utf-8

"""
Redirector tests
"""
from redirector import views


def test_redirects_correctly(client):
    response = client.get('/foo/bar.html?foo=bar')
    assert response.status_code == 301
    assert response.headers['Location'] == 'https://www.example.com/foo/bar.html?foo=bar'


def test_normalize_port_normalizes_properly():
    assert views.normalize_port('http', 80) == None
    assert views.normalize_port('https', 443) == None
    assert views.normalize_port('http', 8080) == 8080
    assert views.normalize_port('http', '8080') == 8080


def test_make_base_url_with_root_base_path():
    scheme = 'https'
    host = 'foo.bar'
    port = 80
    base_path = '/'

    assert views.make_base_url(scheme, host, port, base_path) == 'https://foo.bar:80/'


def test_make_base_url_with_non_root_base_path():
    scheme = 'https'
    host = 'foo.bar'
    port = 80
    base_path = '/fooooooooo/'

    assert views.make_base_url(scheme, host, port, base_path) == 'https://foo.bar:80/fooooooooo/'


def test_make_redirect_url_with_root():
    scheme = 'https'
    host = 'foo.bar'
    port = 80
    base_path = '/aye/aye/captain/'
    path = ''

    expected =  'https://foo.bar:80/aye/aye/captain/'
    assert views.make_redirect_url(path, scheme, host, port, base_path) == expected


def test_make_redirect_url_with_root_base_path():
    scheme = 'https'
    host = 'foo.bar'
    port = 80
    base_path = '/'
    path = 'aye/aye/captain?jump_overboard=true&depth=199'

    expected =  'https://foo.bar:80/aye/aye/captain?jump_overboard=true&depth=199'
    assert views.make_redirect_url(path, scheme, host, port, base_path) == expected


def test_make_redirect_url_with_non_root_base_path():
    scheme = 'https'
    host = 'foo.bar'
    port = 80
    base_path = '/fooooooooo/'
    path = 'aye/aye/captain?jump_overboard=true&depth=199'

    expected =  'https://foo.bar:80/fooooooooo/aye/aye/captain?jump_overboard=true&depth=199'
    assert views.make_redirect_url(path, scheme, host, port, base_path) == expected
