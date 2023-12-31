import asyncio
import logging

from aiogram import Bot, Dispatcher


import config
import handlers

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config.Telegram.token)
    config.Telegram.bot = bot
    dp = Dispatcher()

    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
