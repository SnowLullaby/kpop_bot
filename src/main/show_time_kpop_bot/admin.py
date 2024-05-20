from src.main.show_time_kpop_bot import keyboards, db, text


def start_fnk(bot, user_id, admins_list):
    db.new_user(user_id)
    markup = keyboards.start_admin_keyboard() if user_id in admins_list \
        else keyboards.start_keyboard()
    bot.send_message(user_id, text.start_text(), parse_mode='HTML', reply_markup=markup)


def update_fnk(bot, user_id, admins_list):
    markup = keyboards.admin_main_keyboard() if user_id in admins_list \
        else keyboards.user_main_keyboard()
    bot.send_message(user_id, text.update_text(), parse_mode='HTML', reply_markup=markup)