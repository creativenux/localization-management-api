import os
from supabase import create_client, Client
from typing import List

class LocalizationManager:
    def __init__(self):
        self.client: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

    def create_project(self, project_name: str):
        return self.client.table("projects").insert({"name": project_name}).execute()
    
    def get_projects(self):
        return self.client.table("projects").select("id, name").execute()

    def create_language(self, name: str, code: str):
        return self.client.table("languages").insert({"name": name, "code": code}).execute()
    
    def get_languages(self):
        return self.client.table("languages").select("name, code").execute()
    
    def create_localization(self, project_id: str, key: str, category: str, description: str | None, translations: dict):
        # Convert Translation objects to dictionaries
        translations_dict = {
            lang: {
                "value": trans.value,
                "updated_at": trans.updated_at,
                "updated_by": trans.updated_by
            }
            for lang, trans in translations.items()
        }
        
        return self.client.table("localizations").insert({
            "project_id": project_id,
            "key": key,
            "category": category,
            "description": description,
            "translations": translations_dict
        }).execute()

    def update_localization(self, id: str, project_id: str, translations: dict):
        # Convert Translation objects to dictionaries
        translations_dict = {
            lang: {
                "value": trans.value,
                "updated_at": trans.updated_at,
                "updated_by": trans.updated_by
            }
            for lang, trans in translations.items()
        }
        
        return self.client.table("localizations").update({
            "translations": translations_dict
        }).eq("id", id).eq("project_id", project_id).execute()

    def batch_update_localizations(self, project_id: str, localizations: List[dict]):
        updates = []
        for loc in localizations:
            # Convert Translation objects to dictionaries
            translations_dict = {
                lang: {
                    "value": trans.value,
                    "updated_at": trans.updated_at,
                    "updated_by": trans.updated_by
                }
                for lang, trans in loc.translations.items()
            }
            
            updates.append({
                "id": loc.id,
                "project_id": project_id,
                "translations": translations_dict
            })
        
        # Use upsert to update multiple records
        return self.client.table("localizations").upsert(updates).execute()

    def get_localizations(self, project_id: str):
        return self.client.table("localizations").select("*").eq("project_id", project_id).execute()
    
