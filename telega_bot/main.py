import telebot
from telebot import types
import random

TOKEN="6372635889:AAFgENzKYDCIODifLspIZA8PuRgBcpmH0xQ"

bot = telebot.TeleBot(TOKEN)
keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Play')
btn2 = types.KeyboardButton('No,I pass')
keyboard.add(btn1,btn2)
@bot.message_handler(commands=['start','game'])
def start_message(message):
        bot_message = bot.send_message(message.chat.id,'Привет Чемпион, начнем игру?', reply_markup=keyboard) #бот отправляет сообщение пользователь и дает ему id
        bot.register_next_step_handler(bot_message,check_answer)
def check_answer(message):
    if message.text == 'Play':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1,10)
        print(number)
        game(message,3,number)
    elif message.text == 'No,I pass':
        bot.send_message(message.chat.id, 'Нет так нет,Пока!')
    else:
        bot_message = bot.send_message(message.chat.id,'Вы ввели неправильный ответ!',
        reply_markup=keyboard)
        bot.register_next_step_handler(bot_message,check_answer)
def game(message,attempts,number):
    message_bot = bot.send_message(message.chat.id,"Угадай число")
    bot.register_next_step_handler(message_bot,check_number,attempts-1,number)
def check_number(message,attempts,number):
    if message.text == str(number):
        bot.send_message(message.chat.id,'You win')
    elif attempts == 0:
        bot.send_message(message.chat.id,'You dead')
    else:
        bot.send_message(message.chat.id,'No go again churka')
        game(message,attempts,number)
bot.polling()#запуск бота