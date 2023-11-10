from aiogram import Bot, Dispatcher
from config import Config


bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot)