import telebot
import logging

from src.main.show_time_kpop_bot import text, db, keyboards


def start_bot(new_token, admins_list):
    bot = telebot.TeleBot(new_token)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "/start":
            db.new_user(message.from_user.id)
            markup = keyboards.start_admin_keyboard() if message.from_user.id in admins_list \
                else keyboards.start_keyboard()
            bot.send_message(message.from_user.id, text.start_text(), parse_mode='HTML', reply_markup=markup)

        if message.text == "/help":
            bot.send_message(message.from_user.id, text.help_text(), parse_mode='HTML')

        if message.text == "/update":
            markup = keyboards.admin_main_keyboard() if message.from_user.id in admins_list \
                else keyboards.user_main_keyboard()
            bot.send_message(message.from_user.id, text.update_text(), parse_mode='HTML', reply_markup=markup)

        if message.text == "/add":
            bot.send_message(message.from_user.id, "Для добавления хореографии", parse_mode='HTML')

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "/update":
                bot.send_message(message.from_user.id, "Тестируем обновление", parse_mode='HTML',
                                 reply_markup=keyboards.admin_main_keyboard())
            elif call.data == "/add":
                bot.send_message(message.from_user.id, "Тестируем добавление", parse_mode='HTML')

    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logging.error(f"Connection with bot failed {e}")
        raise
