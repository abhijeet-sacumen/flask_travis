import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<img src="' in response.data

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello world' in response.data
