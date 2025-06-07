import pytest
from fastapi.testclient import TestClient
from src.localization_management_api.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_project_data():
    return {
        "name": "Test Project"
    }

@pytest.fixture
def sample_language_data():
    return {
        "name": "German",
        "code": "de"
    }

@pytest.fixture
def sample_localization_data():
    return {
        "key": "welcome_message",
        "category": "general",
        "description": "Welcome message for users",
        "translations": {
            "de": "Willkommen"
        }
    } 