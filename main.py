import requests
from flask import Flask, request

TOKEN = "8492187656:AAFVYToh_AzzoEJC7Q3_5LqoqX-zcv9m9ZM"
CHANNEL_LINK = "https://t.me/+O6gnTNLs2B45YmYy"
PHOTO_URL = "https://i.ibb.co/WNTmsNwt/photo.jpg"

app = Flask(__name__)

def send_message(chat_id, text, photo_url):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {
        "chat_id": chat_id,
        "caption": text,
        "photo": photo_url
    }
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = (
            "Привет! Я тиктокер с опросами, мемами и приколами.\n\n"
            f"Вот канал с опросами и мемами: {CHANNEL_LINK}\n\n"
            "Заявки в канал принимаются автоматически!"
        )
        send_message(chat_id, text, PHOTO_URL)
    return "ok"

@app.route("/")
def home():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)