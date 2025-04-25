from aiogram import Bot, Dispatcher
import config.settings as set
from app.start.handlers import router as start_router
from app.user.handlers import router as user_router
from app.admin.handlers import router as admin_router
from quiz.app.quiz1.handlers import router as quiz1_router

bot = Bot(token=set.API_TOKEN)
dp = Dispatcher()


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(start_router)
dp.include_router(quiz1_router)


if __name__ == "__main__":
    print("бот запущен")
    dp.run_polling(bot)