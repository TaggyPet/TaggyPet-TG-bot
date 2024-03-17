from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from application.log_config import info_logger

from application.resources.string_consts_config import ABOUT_MESSAGE

menu_router = Router()


@menu_router.message(CommandStart())
async def handle_start_command(message: types.Message):
    info_logger.info(f"User {message.from_user.username} send a start command")
    await message.answer(text="Привет! Выбери команду, которая тебя интересует:")


@menu_router.message(Command("menu"))
async def handle_menu_command(message: types.Message):
    info_logger.info(f"User {message.from_user.username} send a command: {message.text}")
    await message.answer(text="Вот доступные команды:")


@menu_router.message(Command("about"))
async def handle_about_command(message: types.Message):
    await message.answer(text=ABOUT_MESSAGE)
