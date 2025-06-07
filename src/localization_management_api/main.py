from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from typing import List
from .localizationManager import LocalizationManager
from .models import Project, ProjectCreate, Localization, Language, LanguageCreate, LocalizationCreate

app = FastAPI()

localization_manager = LocalizationManager()

@app.get("/projects", response_model=List[Project])
async def get_projects():
    response = localization_manager.get_projects()
    return response.data

@app.post("/projects", response_model=Project)
async def create_project(project: ProjectCreate):
    if not project.name:
        raise HTTPException(status_code=400, detail="Project name is required")
    response = localization_manager.create_project(project.name)
    print('response', response)
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create project")
    return response.data[0]

## This is the endpoint to get the localizations for a project and locale
## It returns a JSON object with the localizations for the project and locale
@app.get("/localizations/{project_id}/{locale}", response_model=List[Localization])
async def get_localizations(project_id: str, locale: str):
    response = localization_manager.get_localizations(project_id, locale)
    return response.data

@app.get("/languages", response_model=List[Language])
async def get_languages():
    response = localization_manager.get_languages()
    return response.data

@app.post("/languages", response_model=Language)
async def create_language(language: LanguageCreate):
    if not language.name or not language.code:
        raise HTTPException(status_code=400, detail="Language name and code are required")
    response = localization_manager.create_language(language.name, language.code)
    if not response.data:
        raise HTTPException(status_code=400, detail="Failed to create language")
    return response.data[0]

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

@app.put("/localizations/{project_id}/{localization_id}", response_model=Localization)
async def update_localization(project_id: str, localization_id: str, localization: LocalizationCreate):
    if not localization.key or not localization.category:
        raise HTTPException(status_code=400, detail="Key and category are required")
    response = localization_manager.update_localization(
        id=localization_id,
        project_id=project_id,
        key=localization.key,
        category=localization.category,
        description=localization.description,
        translations=localization.translations
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="Localization not found")
    return response.data[0]

@app.get("/localizations/{project_id}", response_model=List[Localization])
async def get_localizations(project_id: str):
    response = localization_manager.get_localizations(project_id)
    return response.data
