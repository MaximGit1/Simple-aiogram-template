from aiogram import executor
from create_bot import dp
from handlers import client

def start_bot(dp=dp):
    client.register_handlers_client(dp)
    executor.start_polling(dp)


if __name__ == '__main__':
    start_bot()
