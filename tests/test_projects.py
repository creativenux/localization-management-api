import pytest
from fastapi import status

def test_create_project_success(client, sample_project_data):
    response = client.post("/projects", json=sample_project_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == sample_project_data["name"]
    assert "id" in response.json()

def test_get_projects_after_creation(client, sample_project_data):
    # Create a project first
    client.post("/projects", json=sample_project_data)
    
    # Get all projects
    response = client.get("/projects")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert any(project["name"] == sample_project_data["name"] for project in response.json()) 