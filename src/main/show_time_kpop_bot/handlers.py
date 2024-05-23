import telebot
import logging

from src.main.show_time_kpop_bot import text, admin


def start_bot(new_token, admins_list):
    bot = telebot.TeleBot(new_token)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "/start":
            admin.start_fnk(bot, message.chat.id, message.from_user.id, admins_list)

        if message.text == "/help":
            bot.send_message(message.from_user.id, text.help_text(), parse_mode='HTML')

        if message.text == "/update" or message.text == "Что мы сейчас учим?":
            admin.update_fnk(bot,  message.chat.id, message.from_user.id, admins_list)

        if message.text == "/add" or message.text == "Предложить хорягу":
            bot.send_message(message.from_user.id, "Что бы вы могли предложить свою хореографию", parse_mode='HTML')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "/update":
            admin.update_fnk(bot, call.message.chat.id, call.message.from_user.id, admins_list)
        #if call.data == "/show":
        #    admin.update_fnk(bot, call.message.chat.id, call.message.from_user.id, admins_list)

    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error(f"Connection with bot failed {e}")
        raise
