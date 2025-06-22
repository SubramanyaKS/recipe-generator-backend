from dotenv import load_dotenv
import os

load_dotenv()

API_KEY= os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL")
MAX_TOKEN = os.getenv("MAXTOKEN")
TEMPERATURE=os.getenv("TEMPERATURE")
PORT=os.getenv("PORT")