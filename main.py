# Terminal -> pip install pytelegrambotapi
import telebot
import keyboards
import requests
import random

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
    Что делает бот? - Бот принимает какое-либо изображение, обрабатывает и присылает результат проверки изображения, где указывает на то, что изображено на картинке

    /start - Начать работу
    /help - О работе с ботом

    """, reply_markup=keyboards.menu)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """
    The bot that was created by novice Python programmers:
      Vitya -> Cyber
      Antonis -> sand
      Arkady -> Arkael
      Artem -> Lemon


    Commands:
    -> /random - Присылает рандомное изображение
    -> /4k - Присылает высококачественное изображение
    -> /search - Поиск изображения по ключевому слову

    """)

#конструкция функции
#def название_функции(аргумент):
    #код

#функция обработки
#bot.message_handler(content_type=['команда'])

#функция отправки сообщения пользователя
#bot.send_message(message.chat.id, '')


@bot.message_handler(commands=['random'])
def randoma(message):
    url = requests.get('https://source.unsplash.com/random')
    bot.send_photo(message.chat.id, url.content)

@bot.message_handler(commands=['4k'])
def random4k(message):
    response = requests.get('https://source.unsplash.com/random/4096x2160')
    bot.send_photo(message.chat.id, response.content)
    bot.send_document(message.chat.id, response.content, caption='rename_to_jpg')

@bot.message_handler(commands=['search'])
def search(message):
    msg = bot.send_message(message.chat.id, random.choice(['Напиши ключевые слова: ', 'Введите слова для поиска', 'Введите нужное слово']))
    bot.register_next_step_handler(msg, next_step)

def next_step(message):
    global answer
    answer = message.text
    response = requests.get('https://source.unsplash.com/random?{0}'.format(answer))
    bot.send_photo(message.chat.id, response.content, reply_markup=keyboards.inline_menu)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'stop':
        bot.send_message(call.message.chat.id, 'Прекратил отправку!') # Для вас
    elif call.data == 'next':
        response = requests.get('https://source.unsplash.com/random?{0}'.format(answer))
        bot.send_photo(call.message.chat.id, response.content, reply_markup=keyboards.inline_menu)
    elif call.data == 'random':
        response = requests.get('https://source.unsplash.com/random?{0}')
        bot.send_photo(call.message.chat.id, response.content, reply_markup=keyboards.inline_menu)






bot.polling()