from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from quiz.app.start.db_execute import *
router = Router()

@router.message(Command("start"))
async def admanel(message: Message):
    append_user(message.from_user.id)
    await message.answer("Прверь себя на способность думать с помощью команды /question или добавь меня в чат чтобы доказать тупость своих друзей\n .+/user покажет количество очков набранных вами\n/quiz_1 - quiz без вариантов ответа")
