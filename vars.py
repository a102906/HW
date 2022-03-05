import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

#Telegram bot token
API_TOKEN = '5199501380:AAEUED2ksyLBA34IsMEdS4P2PF1uo506g_s'


#Main menu buttons
menu = KeyboardButton('🗣Начать общение')
creator = KeyboardButton('☎Связь с создателем')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(menu).add(creator)

#Questions or phrases
hi = KeyboardButton('Привет')
name = KeyboardButton('Как тебя зовут?')
joke = KeyboardButton('Расскажи анекдот')
love = KeyboardButton('У тебя есть пара?')
years = KeyboardButton('Сколько тебе лет?')
backToMain = KeyboardButton('↩К началу')
restoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(hi).add(name).add(joke).add(love).add(years).add(backToMain)
