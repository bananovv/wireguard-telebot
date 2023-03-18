import time

import telebot
from telebot import types

bot = telebot.TeleBot('6186694364:AAFxnI-MazFobZbgmW3VqjcJc6lW1Tg1P58')


@bot.message_handler(commands=['start'])
def guide(message):
    msg = f'Привет! Я CloudSupport, надежный и быстрый VPN сервис!'
    bot.send_message(message.chat.id, msg)

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    guide = types.KeyboardButton('Подключить VPN')
    help = types.KeyboardButton('Обратиться в поддержку')
    markup.add(guide, help)
    time.sleep(1)
    msg2 = f'Чтобы начать работу, нажми на одну из кнопок!'
    bot.send_message(message.chat.id, msg2, reply_markup=markup)


@bot.message_handler(regexp='Подключить VPN')
def os(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ios = types.KeyboardButton(text='iOS')
    macos = types.KeyboardButton('MacOS')
    android = types.KeyboardButton('Android')
    win = types.KeyboardButton('Windows')
    alrdy = types.KeyboardButton('Я скачал')
    markup.add(ios, macos, android, win, alrdy)
    msg2 = f'Выбери свое устройство, чтобы скачать клиент WireGuard'
    bot.send_message(message.chat.id, msg2, reply_markup=markup)


@bot.message_handler(regexp='iOS')
def os(message):
    ios = types.InlineKeyboardMarkup()
    ios.add(types.InlineKeyboardButton('Скачать',
                                       url='https://apps.apple.com/ru/app/wireguard/id1441195209?l=en'))

    msg2 = f'WireGuard в AppStore'
    bot.send_message(message.chat.id, msg2, reply_markup=ios)


@bot.message_handler(regexp='MacOS')
def os(message):
    macos = types.InlineKeyboardMarkup()
    macos.add(types.InlineKeyboardButton('Скачать',
                                         url='https://apps.apple.com/ru/app/wireguard/id1451685025?l=en&mt=12'))

    msg2 = f'WireGuard в AppStore'
    bot.send_message(message.chat.id, msg2, reply_markup=macos)


@bot.message_handler(regexp='Android')
def os(message):
    android = types.InlineKeyboardMarkup()
    android.add(types.InlineKeyboardButton('Скачать',
                                           url='https://play.google.com/store/apps/details?id=com.wireguard.android'
                                               '&hl=en_US'))

    msg2 = f'WireGuard в Google Play'
    bot.send_message(message.chat.id, msg2, reply_markup=android)


@bot.message_handler(regexp='Windows')
def os(message):
    win = types.InlineKeyboardMarkup()
    win.add(types.InlineKeyboardButton('Скачать',
                                       url='https://download.wireguard.com/windows-client/wireguard-installer.exe'))

    msg2 = f'WireGuard для Windows'
    bot.send_message(message.chat.id, msg2, reply_markup=win)

@bot.message_handler(regexp='Я скачал')
def os(message):
    win = types.InlineKeyboardMarkup()
    win.add(types.InlineKeyboardButton('Скачать',
                                       url='https://download.wireguard.com/windows-client/wireguard-installer.exe'))

    msg2 = f'ты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гейты гей'
    bot.send_message(message.chat.id, msg2, reply_markup=win)


@bot.message_handler(regexp='Обратиться в поддержку')
def access(message):
    reply_help = f'Надеемся, что ничего страшного не случилось. Вот контакт моего разработчика: t.me/yegorolegovich'
    bot.send_message(message.chat.id, reply_help)


bot.polling(none_stop=True)
