from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def admanel(message: Message):
    await message.answer("Прверь себя на способность думать с помощью команды /question или добавь меня в чат чтобы доказать тупость своих друзей\n /quiz_1 - quiz без вариантов ответа")