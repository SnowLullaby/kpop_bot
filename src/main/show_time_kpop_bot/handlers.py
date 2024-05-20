import telebot
import logging

from src.main.show_time_kpop_bot import text, admin


def start_bot(new_token, admins_list):
    bot = telebot.TeleBot(new_token)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "/start":
            admin.start_fnk(bot, message.from_user.id, admins_list)

        if message.text == "/help":
            bot.send_message(message.from_user.id, text.help_text(), parse_mode='HTML')

        if message.text == "/update" or message.text == "Обновить данные":
            admin.update_fnk(bot, message.from_user.id, admins_list)

        if message.text == "/add" or message.text == "Добавить хореографию":
            bot.send_message(message.from_user.id, "Для добавления хореографии", parse_mode='HTML')

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "/update":
                admin.update_fnk(bot, message.from_user.id, admins_list)
            elif call.data == "/add":
                bot.send_message(message.from_user.id, "Тестируем добавление", parse_mode='HTML')

    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error(f"Connection with bot failed {e}")
        raise
