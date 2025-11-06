# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from bot import handler

import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("bot_token"))
dp = Dispatcher()


async def main():
    dp.include_router(handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
