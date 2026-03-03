import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_homepage_contains_text(client):
    response = client.get("/")
    assert b"Flask" in response.data
