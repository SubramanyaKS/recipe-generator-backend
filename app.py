from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from services import config
from services.api_service import geminiCall
from utils.environment import PORT

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Gemini API Caller",
    description="A simple FastAPI application to interact with Google Gemini API.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    """
    Pydantic model for the request body.
    """
    prompt: str

class RecipeRequest(BaseModel):
    """
    Pydantic model for the recipe request.
    """
    ingredients: str
    cuisine: str

@app.get('/')
async def read_root():
    return {"message": "Welcome to the Gemini API Caller. Use /generate to interact with Gemini."}


@app.post("/api/recipe-generate")
async def generate_recipe_endpoint(request: RecipeRequest):
    """
    Endpoint to generate text using the Gemini API.

    Args:
        request (RecipeRequest): The request body containing the prompt.

    Returns:
        response: A string containing the generated text.
    """
    try:
        prompt =request.ingredients + "\n" + request.cuisine
        print(f"Received ingredients: {request.ingredients}")
        response = geminiCall(prompt)
        print(f"Generated recipe: {response}"   )
        return {"recipe": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling Gemini API: {e}")


@app.post("/api/generate-recipe")
async def generate_recipe_endpoint(request: PromptRequest):
    """
    Endpoint to generate text using the Gemini API.

    Args:
        request (PromptRequest): The request body containing the prompt.

    Returns:
        response: A string containing the generated text.
    """
    try:
        response = geminiCall(request.prompt)
        return {"recipe": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling Gemini API: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
