import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TELEGRAM_KEY")
chat_id = os.environ.get("CHAT_ID")


def send_message():
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    with open("daily_menu.txt", "r") as message:
        requests.post(url, json={'chat_id': chat_id, 'text': message.read()})

