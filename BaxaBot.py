import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from vars import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
intro = 'Здарова, Че хотел?'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(intro, reply_markup=mainmenu)

@dp.message_handler(text = '🗣Начать общение')
async def menuCategories(message: types.Message):
    await message.answer('Выберите фразу', reply_markup=restoMenu)
@dp.message_handler(text = '☎Связь с создателем')
async def cat1Menu(message: types.Message):
    await message.answer('Дядя Баха, сейчас занят')



@dp.message_handler(text = 'Привет')
async def cat1Menu(message: types.Message):
    await message.answer('Здарова, Пупсик')
@dp.message_handler(text = 'Как тебя зовут?')
async def cat1Menu(message: types.Message):
    await message.answer('Если че, я Баха')
@dp.message_handler(text = 'Расскажи анекдот')
async def cat1Menu(message: types.Message):
    await message.answer('Купил у араба часы, а они обратно идут')
@dp.message_handler(text = 'У тебя есть пара?')
async def cat1Menu(message: types.Message):
    await message.answer('Пупсик, ненадо спешить')
@dp.message_handler(text = 'Сколько тебе лет?')
async def cat1Menu(message: types.Message):
    await message.answer('У идеала, нет срока годности')
@dp.message_handler(text = '↩К началу')
async def cat1Menu(message: types.Message):
    await message.answer(intro, reply_markup = mainmenu)



# @dp.message_handler(text= '')
# async def order




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)