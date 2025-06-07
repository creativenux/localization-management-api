import pytest
from fastapi import status

@pytest.fixture
def project_id(client, sample_project_data):
    response = client.post("/projects", json=sample_project_data)
    return response.json()["id"]

def test_get_localizations_empty(client, project_id):
    response = client.get(f"/localizations/{project_id}")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0

def test_create_localization_success(client, project_id, sample_localization_data):
    response = client.post(f"/localizations/{project_id}", json=sample_localization_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["key"] == sample_localization_data["key"]
    assert response.json()["category"] == sample_localization_data["category"]
    assert response.json()["translations"] == sample_localization_data["translations"]
    assert "id" in response.json()

def test_update_localization(client, project_id, sample_localization_data):
    # Create a localization first
    create_response = client.post(f"/localizations/{project_id}", json=sample_localization_data)
    localization_id = create_response.json()["id"]
    
    # Update the localization
    updated_data = sample_localization_data.copy()
    updated_data["translations"]["de"] = "Willkommen Updated"
    
    response = client.put(f"/localizations/{project_id}/{localization_id}", json=updated_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["translations"]["de"] == "Willkommen Updated"

def test_get_localizations_nonexistent_project(client):
    response = client.get("/localizations/nonexistent")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0 
