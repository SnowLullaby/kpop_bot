from src.main.show_time_kpop_bot import keyboards, db, text


def start_fnk(bot, chat_id, user_id, admins_list):
    db.new_user(user_id)
    markup = keyboards.start_admin_keyboard() if user_id in admins_list \
        else keyboards.start_admin_keyboard()
    bot.send_message(chat_id, text.start_text(), parse_mode='HTML', reply_markup=markup)


def update_fnk(bot, chat_id, user_id, admins_list):
    markup = keyboards.admin_main_keyboard() if user_id in admins_list \
        else keyboards.user_main_keyboard()
    bot.send_message(chat_id, text.update_text(db.get_current_choreo()), parse_mode='HTML', reply_markup=markup)
