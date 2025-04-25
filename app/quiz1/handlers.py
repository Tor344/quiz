from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .fms_state import St
from  .db_execute import *


router = Router()


@router.message(Command("quiz_1"))
async def question(message: Message,state: FSMContext):
    question, answer = get_random_question()
    print(question)
    await state.update_data(answer=answer)
    await state.set_state(St.st_answer)
    await message.answer(question)


@router.message(F.text, St.st_answer)
async def question(message: Message,state: FSMContext):
    user_answer = message.text.lower()
    data = await state.get_data()
    print(user_answer,data["answer"])
    if user_answer !=data["answer"]:
        await message.answer(f"Ответ неверный: {data["answer"]} ")
        return
    await state.clear()
    await message.answer("Ответ верный")




