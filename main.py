import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiohttp import web

# === Настройки бота ===
TOKEN = "8492187656:AAFVYToh_AzzoEJC7Q3_5LqoqX-zcv9m9ZM"
CHANNEL_LINK = "https://t.me/+O6gnTNLs2B45YmYy"
PHOTO_URL = "https://i.ibb.co/WNTmsNwt/photo.jpg"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    text = (
        "Привет! Я тиктокер с опросами, мемами и приколами.\n\n"
        f"Вот канал с опросами и мемами: {CHANNEL_LINK}"
    )
    await bot.send_photo(message.chat.id, PHOTO_URL, caption=text)

# === Веб-сервер для Render ===
async def handle(request):
    return web.Response(text="Bot is alive!")

app = web.Application()
app.add_routes([web.get("/", handle)])

async def start_web():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

# Основная функция
async def main():
    await start_web()
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())