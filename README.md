# Mani_TelegramChatBot
# AI-Powered Telegram Chatbot

An intelligent Telegram chatbot built with:
- 🧠 TensorFlow-trained intent model
- 🌐 OpenRouter (Mistral/GPT)
- 🔮 Google Gemini (1.5 Pro)
- 🗣️ NLP using NLTK
- 🤖 Telegram Bot integration
- 🧩 Fallback to APIs: jokes, quotes, riddles, poems, facts

---

## 📌 Features

- Responds using a **locally trained chatbot model** (TensorFlow)
- Falls back to **OpenRouter (Mistral/GPT-4)** or **Google Gemini** if not confident
- Telegram bot replies with:
  - 💬 Text
  - 🎭 Stickers
- Trained on a **custom JSON dataset**
- Modular structure for easy extension

---

## 🛠️ Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| `tensorflow`      | Model training + prediction            |
| `nltk`            | Text processing, lemmatization         |
| `openai`          | OpenRouter API (Mistral, GPT)          |
| `google-generativeai` | Gemini 1.5 Pro integration         |
| `pyTelegramBotAPI`| Telegram bot handling                  |
| `python-dotenv`   | Environment variable management        |

---

## 📁 Project Structure

├── .env # API keys

├── requirements.txt # Dependencies

├── Files/

  │Files/ ├── dataset.json # Custom intents
  
  │Files/ └── data.pickle # Processed NLP data

├── model.keras # Trained TensorFlow model

├── main.py # Telegram bot logic

├── gemini.py # Gemini integration

├── openrouter_ai.py # OpenRouter integration

├── trained_tf_model.py # Chatbot inference logic

├── functions.py # Quotes/Jokes APIs

---

## AUTHOR : Lakshmi Mani Sankar Danda

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash

git clone https://github.com/DandaLakshmiManiSankar/TelegramChatBot.git

cd TelegramChatBot

pip install -r requirements.txt

python train_model.py

python main.py
