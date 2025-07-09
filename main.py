import telebot
import pyfiglet
from pystyle import *
import os
import time
from types import NoneType
import keyboard


def send_message(id_user):
    try:
        text_message = input(Colorate.Horizontal(Colors.red_to_purple, '> '))
        b.send_message(id_user, text_message)
    except:
        pass

try:
    api_token = input(Colorate.Horizontal(Colors.red_to_purple, 'api токен телеграм бота: '))

    b = telebot.TeleBot(api_token)
    print(Colorate.Horizontal(Colors.green_to_yellow, 'бот успешно подключен!'))
except ValueError:
    print(Colorate.Horizontal(Colors.red_to_blue, 'возникла ошибка с токеном, проверь, правильно ли ты его ввел'))
    exit()

time.sleep(3)
os.system('clear')
print(Colorate.Vertical(Colors.red_to_purple, pyfiglet.figlet_format('rew', font='this')))
print(Colorate.Vertical(Colors.red_to_purple, 'тулкит для управления телеграм ботами'))
print(' ')
print(Colorate.Vertical(Colors.red_to_white, Box.DoubleCube('''1. режим сбора информации
2. авто-ответчик
3. спам (может привести к последствиям)
4. сообщение пользователю
''')))
print(' ')
choice = input(Colorate.Horizontal(Colors.red_to_purple, 'выбор: '))

if choice == '1':
    print()
    print(Colorate.Horizontal(Colors.green_to_yellow, 'активирован режим сбора информации, каждое сообщение от пользователей выводится тут'))
    @b.message_handler(content_types=['text'])
    def text(message):
        username = '@' + str(message.from_user.username)
        fnln = message.from_user.first_name + ' ' + str(message.from_user.last_name)
        idd1 = message.from_user.id
        if type(message.from_user.username) == NoneType:
            username = 'отсутствует'
        if type(message.from_user.last_name) == NoneType:
            fnln = message.from_user.first_name

        print(f'{fnln}(id: {idd1}, юзернейм: {username}): {message.text}')

    b.infinity_polling()
if choice == '2':
    print()
    print(Colorate.Horizontal(Colors.green_to_yellow,'активирован режим авто-ответчика, на любое сообщение будет приходить один и тот же ответ'))
    text = input(Colorate.Horizontal(Colors.red_to_purple, 'что будет отвечать бот: '))
    @b.message_handler(content_types=['text'])
    def reply(message):

        username = '@' + str(message.from_user.username)
        fnln = message.from_user.first_name + ' ' + str(message.from_user.last_name)
        idd1 = message.from_user.id
        if type(message.from_user.username) == NoneType:
            username = 'отсутствует'
        if type(message.from_user.last_name) == NoneType:
            fnln = message.from_user.first_name

        b.reply_to(message, text)
        print(f'{fnln}(id: {idd1}, юзернейм: {username}): {message.text}')
    b.infinity_polling()
if choice == '3':
    print()
    print(Colorate.Horizontal(Colors.green_to_yellow,'активирован режим спама, надеюсь, ты понимаешь что ставишь под риск свой аккаунт, будь аккуратен'))
    text = input(Colorate.Horizontal(Colors.red_to_purple, 'текст для спама: '))
    id = input(Colorate.Horizontal(Colors.red_to_purple, 'id чата или пользователя куда нужно спамить: '))
    tm = input(Colorate.Horizontal(Colors.red_to_purple, 'задержка в секундах: '))
    tms = input(Colorate.Horizontal(Colors.red_to_purple, 'количество повторений (напиши "while" если нужно без остановки): '))
    if tms != 'while':
        for q in range(int(tms)):
            b.send_message(id, text)
            time.sleep(float(tm))
    else:
        while True:
            b.send_message(id, text)
            time.sleep(float(tm))
if choice == '4':
    print(Colorate.Horizontal(Colors.green_to_yellow,
                              'выбрана функция отправки сообщения'))
    idd = input(Colorate.Horizontal(Colors.red_to_purple, 'id пользователя которому нужно отправить сообщение: '))
    msgg = input(Colorate.Horizontal(Colors.red_to_purple, 'сообщение: '))
    try:
        b.send_message(idd, msgg)
    except:
        print(Colorate.Horizontal(Colors.red_to_blue, 'возникла ошибка с отправкой, проверь, правильно ли ты все написал'))
    
    
   



