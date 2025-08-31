import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# === Настройки бота ===
TOKEN = "8492187656:AAFVYToh_AzzoEJC7Q3_5LqoqX-zcv9m9ZM"
CHANNEL_LINK = "https://t.me/+O6gnTNLs2B45YmYy"
PHOTO_URL = "https://i.ibb.co/WNTmsNwt/photo.jpg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    text = (
        "Привет! Я тиктокер с опросами, мемами и приколами.\n\n"
        f"Вот канал с опросами и мемами: {CHANNEL_LINK}"
    )
    await message.answer_photo(PHOTO_URL, caption=text)

# === Веб-сервер для UptimeRobot/Replit ===
async def handle(request):
    return web.Response(text="Bot is alive!")

app = web.Application()
app.add_routes([web.get("/", handle)])

async def start_web():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(app, "0.0.0.0", 8080)
    await site.start()

# Основная функция
async def main():
    await start_web()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())