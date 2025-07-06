import telebot
import pyfiglet
from pystyle import *
import os
import time
from types import NoneType
try:
    api_token = input(Colorate.Horizontal(Colors.red_to_purple, 'api токен телеграм бота: '))

    b = telebot.TeleBot(api_token)
    print(Colorate.Horizontal(Colors.green_to_yellow, 'бот успешно подключен!'))
except ValueError:
    print(Colorate.Horizontal(Colors.red_to_blue, 'возникла ошибка с токеном, проверь, правильно ли ты его ввел'))
    exit()

time.sleep(3)
os.system('cls')
print(Colorate.Vertical(Colors.red_to_purple, pyfiglet.figlet_format('rew', font='this')))
print(Colorate.Vertical(Colors.red_to_purple, 'тулкит для управления телеграм ботами и готовыми скриптами'))
print(' ')
print(Colorate.Vertical(Colors.red_to_white, Box.DoubleCube('''1. режим сбора информации
2. авто-ответчик
3. спам (может привести к последствиям)
4. чат с определенным пользователем
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
                              'активирован режим чата с определенным пользователем'))
    idd = input(Colorate.Horizontal(Colors.red_to_purple, 'id пользователя с которым ты хочешь ввести диалог: '))
    textt1 = input(Colorate.Horizontal(Colors.red_to_purple, 'текст для начала чата (нечего не пиши чтобы промолчать): '))

    if textt1 != '':
        b.send_message(int(idd), textt1)
        print(Colorate.Horizontal(Colors.green_to_yellow,
                                  'отправлено, ожидай ответ'))
    else:
        print(Colorate.Horizontal(Colors.green_to_yellow,
                                  'ты промолчал, жди сообщения'))
    @b.message_handler(content_types=['text'])
    def texttt(message):
        if message.from_user.id == int(idd):
            username = '@' + str(message.from_user.username)
            fnln = message.from_user.first_name + ' ' + str(message.from_user.last_name)
            idd1 = message.from_user.id
            if type(message.from_user.username) == NoneType:
                username = 'отсутствует'
            if type(message.from_user.last_name) == NoneType:
                fnln = message.from_user.first_name

            print(f'{fnln}(id: {idd1}, юзернейм: {username}): {message.text}')
            textt = input(Colorate.Horizontal(Colors.red_to_purple, 'текст для ответа (нечего не пиши чтобы промолчать): '))
            if textt != '':
                b.send_message(message.chat.id, textt)
            else:
                pass
        else:
            pass
    b.infinity_polling()



