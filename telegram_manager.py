import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_report(message_text):
    """
    Sends the briefing text to your Telegram (Phone + Laptop).
    """
    if not TOKEN or not CHAT_ID:
        return "Error: Telegram keys missing."

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message_text,
        "parse_mode": "Markdown" # Allows bolding/styling
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return "Briefing sent to Telegram secure line."
        else:
            print(f"Telegram Error: {response.text}")
            return "Could not reach Telegram servers."
            
    except Exception as e:
        print(f"Telegram Connection Error: {e}")
        return "Telegram connection failed."