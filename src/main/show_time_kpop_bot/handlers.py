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

        if message.text == "/update" or message.text == "Что мы сейчас учим?":
            admin.update_fnk(bot,  message.from_user.id, admins_list)

        if message.text == "/show":
            admin.show_fnk(bot, message.from_user.id)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "/update":
            admin.update_fnk(bot, call.message.chat.id, admins_list)
        if call.data == "/show_all":
            admin.show_all(bot, call.message.chat.id)
        if call.data == "/show_waiting":
            admin.show_waiting(bot, call.message.chat.id)
        if call.data == "/show_learned":
            admin.show_learned(bot, call.message.chat.id)

    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error(f"Connection with bot failed {e}")
        raise
