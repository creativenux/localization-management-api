from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .localizationManager import LocalizationManager
from .models import Project, ProjectCreate, Localization, Language, LanguageCreate, LocalizationCreate, LocalizationUpdate, BatchLocalizationUpdate

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

localization_manager = LocalizationManager()

# Get all projects
@app.get("/")
async def index():
    return {"message": "Welcome to the Localization Management API"}

# Get all projects
@app.get("/projects", response_model=List[Project])
async def get_projects():
    response = localization_manager.get_projects()
    return response.data

# Create a new project
@app.post("/projects", response_model=Project)
async def create_project(project: ProjectCreate):
    if not project.name:
        raise HTTPException(status_code=400, detail="Project name is required")
    response = localization_manager.create_project(project.name)
    print('response', response)
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create project")
    return response.data[0]

# Get all supported languages
@app.get("/languages", response_model=List[Language])
async def get_languages():
    response = localization_manager.get_languages()
    return response.data

# Create a new language
@app.post("/languages", response_model=Language)
async def create_language(language: LanguageCreate):
    if not language.name or not language.code:
        raise HTTPException(status_code=400, detail="Language name and code are required")
    response = localization_manager.create_language(language.name, language.code)
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create language")
    return response.data[0]

# Create a new localization entry for a project
@app.post("/localizations/{project_id}", response_model=Localization)
async def create_localization(project_id: str, localization: LocalizationCreate):
    if not localization.key or not localization.category:
        raise HTTPException(status_code=400, detail="Key and category are required")
    response = localization_manager.create_localization(
        project_id=project_id,
        key=localization.key,
        category=localization.category,
        description=localization.description,
        translations=localization.translations
    )
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create localization")
    return response.data[0]

# Update multiple localizations in a project in batch
@app.put("/localizations/{project_id}/batch", response_model=List[Localization])
async def batch_update_localizations(project_id: str, updates: BatchLocalizationUpdate):
    print('Received updates:', updates.model_dump())
    response = localization_manager.batch_update_localizations(
        project_id=project_id,
        localizations=updates.localizations
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="No localizations were updated")
    return response.data

# Update a specific localization entry
@app.put("/localizations/{project_id}/{localization_id}", response_model=Localization)
async def update_localization(project_id: str, localization_id: str, localization: LocalizationUpdate):
    response = localization_manager.update_localization(
        id=localization_id,
        project_id=project_id,
        translations=localization.translations
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="Localization not found")
    return response.data[0]

# Get all localizations for a specific project
@app.get("/localizations/{project_id}", response_model=List[Localization])
async def get_localizations(project_id: str):
    response = localization_manager.get_localizations(project_id)
    return response.data
