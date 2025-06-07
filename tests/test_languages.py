import pytest
from fastapi import status

def test_get_languages_empty(client):
    response = client.get("/languages")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)

def test_create_language_success(client, sample_language_data):
    response = client.post("/languages", json=sample_language_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == sample_language_data["name"]
    assert response.json()["code"] == sample_language_data["code"]
    assert "code" in response.json()

def test_get_languages_after_creation(client, sample_language_data):
    # Create a language first
    client.post("/languages", json=sample_language_data)
    
    # Get all languages
    response = client.get("/languages")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert any(lang["name"] == sample_language_data["name"] and 
              lang["code"] == sample_language_data["code"] 
              for lang in response.json()) 