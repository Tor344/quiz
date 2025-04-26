from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from quiz.app.user.db_execute import *

router = Router()

@router.message(Command("user"))
async def user_panel(message: Message):
    await message.answer(f"Вы набрали за всю игру {get_point_user(message.from_user.id)} очков")
