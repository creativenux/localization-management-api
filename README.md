# Localization Management API

A localization management backend built with FastAPI and Supabase, designed to handle multiple projects and languages efficiently.

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Supabase**: PostgreSQL-based backend for storing projects, languages, and translations
- **Python 3.12+**: Latest Python version for optimal performance
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for high-performance async operations

## Performance Considerations

2. **API Design**
   - RESTful endpoints with clear naming conventions
   - Comprehensive error handling and validation
   - CORS enabled for cross-origin requests

3. **Developer Experience**
   - Type hints and Pydantic models for better code maintainability
   - Clear API documentation with FastAPI's automatic OpenAPI generation

## Project Development Time

This project was developed over approximately 5 hours, exceeding the initial 2-3 hour estimate. The additional time was invested in ensuring code quality and maintainability.

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/creativenux/localization-management-api.git
```

2. **Environment Setup**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory with:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_secret_key # NOT anon key
   ```

5. **Run the Server**
   ```bash
   uvicorn src.localization_management_api.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://127.0.0.1:8000/docs`
- Alternative API documentation: `http://127.0.0.1:8000/redoc`

## Testing

Run the test suite with:
```bash
# Basic test run
pytest

# Detailed test output
pytest -v

# Test coverage report
pytest --cov=src
```

## Example Usage

### Create Project
```bash
POST http://127.0.0.1:8000/projects
{
    "name": "My Project"
}
```

### Add Language
```bash
POST http://127.0.0.1:8000/languages
{
    "name": "English",
    "code": "en"
}
```

### Batch Update Localizations
```bash
PUT http://127.0.0.1:8000/localizations/{project_id}/batch
{
    "localizations": [
        {
            "id": "localization_id",
            "translations": {
                ...existing_translations,
                "en": {
                    "value": "Hello",
                    "updated_at": "2024-03-20T12:00:00Z",
                    "updated_by": "user_id"
                }
            }
        },
    ]
}
```
