import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API setup
openai.api_key = api_key
openai.api_base = "https://openrouter.ai/api/v1"

# Model - you can change this
#MODEL_NAME = "openai/gpt-4"
MODEL_NAME="mistralai/mistral-7b-instruct"
def genAI(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        text = response["choices"][0]["message"]["content"]
        return {"text": [text], "sticker": "", "audio": ""}
    except Exception as e:
        print("OpenRouter Error:", e)
        return {"text": ["Something went wrong"], "sticker": "", "audio": ""}
