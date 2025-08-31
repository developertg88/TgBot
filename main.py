import time
import requests

TOKEN = "8492187656:AAFVYToh_AzzoEJC7Q3_5LqoqX-zcv9m9ZM"
CHANNEL_LINK = "https://t.me/+O6gnTNLs2B45YmYy"
PHOTO_URL = "https://i.ibb.co/WNTmsNwt/photo.jpg"

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    if offset:
        url += f"?offset={offset}"
    r = requests.get(url).json()
    return r["result"]

def send_message(chat_id, text, photo_url):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {
        "chat_id": chat_id,
        "caption": text,
        "photo": photo_url
    }
    requests.post(url, data=data)

offset = None
print("Bot is running...")

while True:
    updates = get_updates(offset)
    for update in updates:
        offset = update["update_id"] + 1
        if "message" in update and "text" in update["message"]:
            msg_text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            
            if msg_text.lower() == "/start":
                text = (
                    "Привет! Я тиктокер с опросами, мемами и приколами.\n\n"
                    f"Вот канал с опросами и мемами: {CHANNEL_LINK}\n\n"
                    "Заявки в канал принимаются автоматически!"
                )
                send_message(chat_id, text, PHOTO_URL)
    time.sleep(2)