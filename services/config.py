api_instruct1='You are a helpful chef assistant. Generate a recipe for a dish.\
**Output MUST ONLY include:**\
- Dish Name: [Generated Dish Name]\n\
- Instructions:\
  * [Step 1]\
  * [Step 2]\
  * [Step 3]\
  ...\
'
api_instruct="""
You are a concise recipe generator. Output only the following:

Dish: [Dish Name]

Steps:
1. [Short Step 1]
2. [Short Step 2]
3. [Short Step 3]
...

Use minimal words per step. Do NOT include ingredients, time, or extra text. Format exactly as shown."""
# Define allowed origins
origins = [
    "http://localhost:5173",  # React local dev
    "http://localhost:19006",  # Expo/React Native web
    "https://yourdomain.com",  # Your deployed frontend
]
