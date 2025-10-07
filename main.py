import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from handlers import user_handlers

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(user_handlers.router)

logging.basicConfig(level=logging.INFO)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())