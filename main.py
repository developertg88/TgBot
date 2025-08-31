import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiohttp import web

TOKEN = "8492187656:AAFVYToh_AzzoEJC7Q3_5LqoqX-zcv9m9ZM"
CHANNEL_LINK = "https://t.me/+O6gnTNLs2B45YmYy"
PHOTO_URL = "https://i.ibb.co/WNTmsNwt/photo.jpg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔥 Перейти на канал", url=CHANNEL_LINK)]
        ]
    )

    text = (
        "👋 Привет!\n\n"
        "Я тиктокер, который делает **смешные опросы** и не только!\n\n"
        "✅ У нас есть приколы, мемы и ты тоже можешь **поучаствовать в моих видосах**!\n\n"
        f"👉 Вот мой канал с опросами и мемами:\n{CHANNEL_LINK}\n\n"
        "Заходи прямо сейчас! 🚀"
    )

    await message.answer_photo(photo=PHOTO_URL, caption=text, reply_markup=keyboard, parse_mode="Markdown")

# Веб-сервер для Render
async def handle(request):
    return web.Response(text="Bot is alive!")

app = web.Application()
app.add_routes([web.get("/", handle)])

async def start_web():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

async def main():
    await start_web()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())