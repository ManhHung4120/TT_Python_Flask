import pytest
from app import app as test_flask


@pytest.fixture
def app():
    yield test_flask


@pytest.fixture
def client(app):
    return app.test_client()
