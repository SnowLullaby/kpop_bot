from telebot import types


def user_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    key_upd = types.InlineKeyboardButton(text='Обновить', callback_data='/update')
    keyboard.add(key_upd)
    key_add = types.InlineKeyboardButton(text='Предложить хореографию', callback_data='/add')
    keyboard.add(key_add)
    return keyboard


def admin_main_keyboard():
    keyboard = user_main_keyboard()
    key_mailing = types.InlineKeyboardButton(text='Написать рассылку', callback_data='/mailing')
    keyboard.add(key_mailing)
    key_status = types.InlineKeyboardButton(text='Изменить статус хореографии', callback_data='/status')
    keyboard.add(key_status)
    return keyboard


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
