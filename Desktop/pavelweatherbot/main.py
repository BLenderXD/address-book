import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from database import create_tables
from handlers import router

# Настройки логирования
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Токен бота
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Создание бота с правильным parse_mode для aiogram 3.7+
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'), default=DefaultBotProperties(parse_mode="HTML"))

# Создание диспетчера и хранилища
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Функция запуска бота
def main():
    create_tables()  # Создаём таблицы в БД
    dp.include_router(router)  # Подключаем маршруты
    dp.run_polling(bot, skip_updates=True)  # Запускаем бота в режиме polling

if __name__ == "__main__":
    main()
