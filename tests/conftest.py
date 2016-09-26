# coding=utf-8
import pytest
from redirector import create_app

@pytest.fixture
def app():
    app = create_app()
    return app
