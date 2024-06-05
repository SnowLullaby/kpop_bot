from telebot import types


def user_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_upd = types.KeyboardButton(text='Что мы сейчас учим?')
    key_add = types.KeyboardButton(text='Добавить хорягу')
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
    return keyboard


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    key_upd = types.InlineKeyboardButton(text='Что мы сейчас учим?', callback_data='/update')
    # key_show = types.InlineKeyboardButton(text='Уже выучили', callback_data='/show')
    keyboard.add(key_upd)
    return keyboard


def show_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    key_all = types.InlineKeyboardButton(text='Все', callback_data='/show_all')
    key_waiting = types.InlineKeyboardButton(text='Предложенные', callback_data='/show_waiting')
    key_learned = types.InlineKeyboardButton(text='Выученные', callback_data='/show_learned')
    keyboard.add(key_all, key_waiting, key_learned)
    return keyboard
