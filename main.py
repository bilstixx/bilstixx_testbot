from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # токен хранится в Render

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я IELTS бот. Хочешь начать Speaking практику?")

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer("Команды:\n/start — начать\n/help — помощь")

if __name__ == "__main__":
    executor.start_polling(dp)
