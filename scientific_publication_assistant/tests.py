import pytest as pytest
from django.test import TestCase
from django.test import Client


@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def test_publication_view(client):
    client.login(username='anna', password='1234')
    response = client.get('/master_publication/2/')
    assert response.status_code == 200
