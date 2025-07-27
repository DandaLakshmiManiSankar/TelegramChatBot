from telebot import TeleBot
from functions import Facts, APIS
from trained_tf_model import chat_with_trained_model
from dotenv import dotenv_values
from gemini import genAI
from openrouter_ai import genAI

import os
from dotenv import load_dotenv
from telebot import TeleBot

# Load .env file
load_dotenv()
BOT_API="8491578357:AAEKkvZmXGnGrVZUwMmVCU971NWmr6H97vA"
# Get the token from environment
API = "8491578357:AAEKkvZmXGnGrVZUwMmVCU971NWmr6H97vA"
#bot = telebot.TeleBot("8491578357:AAHPzzlb0QLE8L874acz_CO7syIrtfRzWCk")


# Initialize bot
BOT = TeleBot(API)



def trainedModel(prompt: str):
    try :
        response, context = chat_with_trained_model(prompt)
        if response is None and context is None:
            return None
        elif context == "quote":
            return APIS.getQuotes()
        elif context == "joke":
            return APIS.getJokes()
        elif context == "fact":
            value = Facts.getFacts(prompt)
            return value
        elif context == "poem":
            return APIS.getPoems()
        elif context == "riddle":
            return APIS.getRiddles()
        elif context == "again":
            pass
        else:
            return response
    except :
        return None


def AI_models(prompt: str) -> dict:
    try:
        response = trainedModel(prompt)
        if response is None:
            return genAI(prompt)
        else:
            return response
    except Exception as e:
        print(e)
        return {"text": ["Something went wrong"], "sticker": "", "audio": ""}


@BOT.message_handler(commands=["start"])
def welcomeMessege(message):
    text = f"Your Chat Id is {message.chat.id}\nPlease link your Mili account with Chat Id for better experience"
    BOT.reply_to(message, text)


@BOT.message_handler(func=lambda msg: True)
def sendMessage(message):
    try:
        response = AI_models(message.text.lower())
        text = response.get("text")
        sticker = response.get("sticker")
        audio = response.get("audio")

        if sticker != "":
            BOT.send_sticker(message.chat.id, sticker=sticker)
        if audio != "":
            BOT.send_audio(message.chat.id, audio=audio)
        if len(text) == 1:
            BOT.reply_to(message, text[0])
        else:
            for text in text:
                BOT.send_message(message.chat.id, text)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    print("Bot has been be initialized")
    BOT.infinity_polling()
