from google import genai
from google.genai import types

from services import config
from utils.environment import API_KEY, MAX_TOKEN, MODEL, TEMPERATURE

client = genai.Client(api_key=API_KEY)

def geminiCall(prompt:str)->str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=config.api_instruct,
            max_output_tokens=MAX_TOKEN,
            temperature=TEMPERATURE,
        )
    )
    if not response:
        return 'No Recipe Generated'
    
    generated_recipe = response.text
    return generated_recipe
