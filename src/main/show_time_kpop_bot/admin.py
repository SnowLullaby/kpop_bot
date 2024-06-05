from src.main.show_time_kpop_bot import keyboards, db, text


def start_fnk(bot, user_id, admins_list):
    db.new_user(user_id)
    markup = keyboards.start_admin_keyboard() if user_id in admins_list \
        else keyboards.start_admin_keyboard()
    bot.send_message(user_id, text.start_text(), parse_mode='HTML', reply_markup=markup)


def update_fnk(bot, user_id, admins_list):
    markup = keyboards.admin_main_keyboard() if user_id in admins_list \
        else keyboards.user_main_keyboard()
    bot.send_message(user_id, text.update_text(db.get_choreo(7)), parse_mode='HTML', reply_markup=markup)


def show_fnk(bot, user_id):
    markup = keyboards.show_keyboard()
    bot.send_message(user_id, text.show_start_text(), parse_mode='HTML', reply_markup=markup)


def show_all(bot, user_id):
    bot.send_message(user_id, text.show_all(db.get_choreo(-10)), parse_mode='HTML')


def show_waiting(bot, user_id):
    bot.send_message(user_id, text.show_all(db.get_choreo(10)), parse_mode='HTML')


def show_learned(bot, user_id):
    bot.send_message(user_id, text.show_all(db.get_choreo(6)), parse_mode='HTML')
