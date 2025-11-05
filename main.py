# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from bot import config, handler

bot = Bot(token=config.Tg_Config().bot_token)
dp = Dispatcher()


async def main():
    dp.include_router(handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
