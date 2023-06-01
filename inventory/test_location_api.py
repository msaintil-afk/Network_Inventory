from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_get_all_device_locations(api_client):
    url = reverse('location-list-create')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 0  # Assuming no locations are present initially

# Add more test functions for other endpoints

