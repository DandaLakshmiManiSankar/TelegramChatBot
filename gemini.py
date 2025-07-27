import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
GEMINI_API_KEY= Enter GeniniAPI Key without any quotes
api_key1 = os.getenv("GEMINI_API_KEY")  # ✅ Fetch key by variable name

genai.configure(api_key=api_key1)  # Configure Gemini with key

model = genai.GenerativeModel("models/gemini-1.5-pro")

def genAI(prompt):
    try:
        response = model.generate_content(prompt)
        return {"text": [response.text], "sticker": "", "audio": ""}
    except Exception as e:
        print("Gemini Error:", e)
        return {"text": ["Something went wrong"], "sticker": "", "audio": ""}
