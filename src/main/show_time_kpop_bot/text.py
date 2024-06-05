def start_text():
    return ('Добро пожаловать в бот K-pop группы танцевальной студии\n<strong><em>&#127800; Show '
            'Time &#127800;</em></strong>.\n\nЗдесь вы найдете:\n'
            '&#10004; Актуальную хорягу\n'
            '&#10004; Все, что мы уже выучили\n&#10004; Голосование за '
            'следующую хорягу\n\nХочешь узнать, что умеет бот? Введи /help или посмотри в меню')


def help_text():
    return ('Доступные команды:\n\n'
            '/start - зарегистрироваться. ты уже это сделал(а) :3\n'
            '/help - получить список команд\n'
            '/update - получить информацию о хоряга, которую мы учим сейчас\n'
            '/add - предложить хорягу (временно не работает)\n'
            '/vote - проголосовать за понравившуюся хорягу (временно не работает)\n'
            '/rating - посмотреть рейтинг хоряг (временно не работает)\n'
            '/mailing - начать рассылку перед занятием (для администраторов, временно не работает)\n'
            '/status - установить статус для хоряги (для администраторов, временно не работает)')


def update_text(choreo_list):
    text = 'Сейчас мы учим: \n\n'
    counter = 1
    if choreo_list is None:
        return ('Сейчас мы ничего не учим, но обязательно скоро начнем новую хорягу :3 \n Внимательно следи за '
                'обновлениями')
    for choreo in choreo_list:
        new_text = (f'&#127800; {choreo[1]} от группы {choreo[0]} &#127800;\n'
                    f'c {format_time(choreo[2])} до {format_time(choreo[3]) if choreo[3] is not None
                    else "как пойдет"}\n'
                    f'Ссылка на хорягу: {str(choreo[4])}\n')
        text += new_text
        counter += 1
        break
    return text


def format_time(time_obj):

    if time_obj.hour == 0:
        return time_obj.strftime('%M:%S')
    else:
        return time_obj.strftime('%H:%M:%S')


def show_start_text():
    return 'Какие хоряги хочешь посмотреть?'


def show_all(choreo_list):
    return 'dgfgf'