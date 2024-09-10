import pytest
from app import create_app

# pytest tests/test_auth.py -v

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_user_register(client):
    response = client.post('/auth/register', json={
        'user_id': '1'
    }, headers={"Content-Type": "application/json"})
    assert response.status_code == 200

def test_login(client):
    response = client.post('/auth/login', json={
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMSJ9.TcXz_IwlmxO5nPd3m0Yo67WyYptabkqZW4R9HNwPmKE'
    }, headers={"Content-Type": "application/json"})
    assert response.status_code == 200