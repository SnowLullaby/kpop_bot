import telebot
import logging

from src.main.show_time_kpop_bot import text, db


def start_bot(new_token):
    bot = telebot.TeleBot(new_token)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "/start":
            db.new_user(message.from_user.id)
            bot.send_message(message.chat.id, text.start(), parse_mode='HTML')
        if message.text == "/help":
            bot.send_message(message.chat.id, "Проверяем помощь", parse_mode='HTML')

    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error(f"Connection with bot failed {e}")
        raise
