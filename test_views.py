import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse

client = Client()


@pytest.mark.django_db
def test_master_publication_list_view(client):
    client.login(username='anna', password='1234')
    response = client.get("/master_publication/1/")
    assert response.status_code == 200


def test_welcome_view(client):
    url = reverse('welcome-view')
    response = client.get(url)
    assert response.status_code == 200
