from pydantic import BaseModel
from typing import List

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: str

    class Config:
        from_attributes = True

class Translation(BaseModel):
    value: str
    updated_at: str
    updated_by: str

class LocalizationBase(BaseModel):
    key: str
    category: str
    description: str | None = None
    translations: dict[str, Translation]

class LocalizationCreate(LocalizationBase):
    pass

class LocalizationUpdate(BaseModel):
    translations: dict[str, Translation]

class BatchLocalizationUpdate(BaseModel):
    localizations: List[dict[str, str | dict[str, Translation]]]  # List of dicts with id and translations

class Localization(LocalizationBase):
    id: int
    project_id: str

    class Config:
        from_attributes = True

class LanguageBase(BaseModel):
    name: str
    code: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    pass
