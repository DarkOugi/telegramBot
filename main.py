import logging
from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token_key

API_TOKEN = telegram_token_key
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'about'])
async def start_dialog(message: types.Message):
    print(message)
    dict_command = {
        '/start': f'Привет,{message.chat.username}, я Ougi, бот для анализа настроений в твоих сообщениях.\n'
                  f' Просто напиши любой текст, а я подумаю над его настроением',
        '/about': 'Я написан на языке Python, с помощью асинхронного телеграмм бота aiogram, а в моем мл '
                  'применялся руссаязычный Bert и библиотека Pytorch'}
    await message.reply(dict_command[message.text])


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await message.answer(message.text)

@dp.message_handler()
async def errors(message: types.File):
    print(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
