from telebot import types


def user_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_upd = types.KeyboardButton(text='Обновить данные')
    key_add = types.KeyboardButton(text='Добавить хореографию')
    markup.add(key_upd, key_add)
    return markup


def admin_main_keyboard():
    markup = user_main_keyboard()
    key_mailing = types.KeyboardButton(text='Написать рассылку')
    key_status = types.KeyboardButton(text='Изменить статус хореографии')
    markup.add(key_mailing, key_status)
    return markup


def start_admin_keyboard():
    keyboard = start_keyboard()
    key_mailing = types.InlineKeyboardButton(text='Написать рассылку', callback_data='/mailing')
    keyboard.add(key_mailing)
    key_status = types.InlineKeyboardButton(text='Изменить статус хореографии', callback_data='/status')
    keyboard.add(key_status)
    return keyboard


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    key_upd = types.InlineKeyboardButton(text='Что мы сейчас учим?', callback_data='/update')
    keyboard.add(key_upd)
    return keyboard
