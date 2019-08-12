import pytest

from app import create_app

@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""

    app = create_app(config={ 'TESTING': True })
    client = app.test_client()

    yield client


def test_universities(client):
    response = client.get("/api/v1/universities/")
    assert response.status_code == 200
