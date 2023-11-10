from aiogram import types, Dispatcher
from create_bot import dp, bot

#@dp.message_handler()
async def command_start(message: types.Message):
    await message.answer(text= "Я ничего не умею")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])