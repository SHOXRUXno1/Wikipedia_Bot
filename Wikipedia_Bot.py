import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT_TOKEN'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nMen Wikipedia Botiman!\naiogramda yaratilganman.")


@dp.message_handler()
async def get_data(message: types.Message):
    matn = message.text
    await message.answer(wikipedia.summary(matn))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
