# Recipe Generator Backend

This is the backend service for the Recipe Generator application. It leverages [FastAPI](https://fastapi.tiangolo.com/) for building APIs and integrates with Google's Gemini model for AI-powered recipe generation.

## Features

- Generate recipes based on user-provided ingredients or preferences
- AI-powered suggestions using Gemini
- RESTful API endpoints with FastAPI
- Easy to deploy and extend

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Gemini API client (or relevant SDK)
- Other dependencies in `requirements.txt`

## Installation

```bash
git clone https://github.com/SubramanyaKS/recipe-generator-backend.git
cd recipe-generator-backend
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn main:app --reload
```

## API Endpoints

- `POST /generate-recipe`  
    Generate a recipe based on input ingredients or preferences.

## Configuration

Set your Gemini API credentials as environment variables or in a `.env` file.

## License

MIT License

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Gemini](https://ai.google.dev/gemini-api/docs)