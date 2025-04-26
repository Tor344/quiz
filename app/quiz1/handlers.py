from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import random

from quiz.app.quiz1.fms_state import St
from quiz.app.quiz1.db_execute import *
from quiz.app.quiz1.ckoreckt_answer import text_ckoreckt


router = Router()


@router.message(Command("quiz_1"))
async def question(message: Message,state: FSMContext):
    question, answer = get_random_question()
    await state.update_data(answer=answer)
    await state.set_state(St.st_answer)
    await message.answer(question)


@router.message(F.text, St.st_answer)
async def question(message: Message,state: FSMContext):
    user_answer = message.text.lower()
    data = await state.get_data()
    if not(text_ckoreckt(user_answer,data["answer"])):
        await message.answer(f"Ответ неверный: {data["answer"]} ")
        return
    await state.clear()
    up_point(message.from_user.id)
    await message.answer("Ответ верный")


@router.message(F.text)
async def question(message: Message,state: FSMContext):
    if  random.random() > 0.1:
        return
    question, answer = get_random_question()
    await state.update_data(answer=answer)
    await state.set_state(St.st_answer)
    await message.answer(question)



