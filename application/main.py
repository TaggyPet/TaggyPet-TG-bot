import asyncio

from dotenv import dotenv_values
from aiogram import Bot, Dispatcher

from application.log_config import info_logger
from application.log_config import error_logger

from application.handlers.menu_router import menu_router

# ENVIRONMENTS
dotenv_config = dotenv_values("resources/env/.env.dev")
BOT_TOKEN = dotenv_config["BOT_TOKEN"]

# TELEGRAM BOT
bot = Bot(BOT_TOKEN)
dispatcher = Dispatcher()

dispatcher.include_routers(menu_router)


async def bot_initialization():
    await dispatcher.start_polling(bot)


def application_entrypoint():
    try:
        info_logger.info("Bot successfully initialized")
        asyncio.run(bot_initialization())
    except KeyboardInterrupt:
        error_logger.error("1234")


if __name__ == "__main__":
    application_entrypoint()
