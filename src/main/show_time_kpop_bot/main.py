import logging
import os
import sys
import psycopg2
import telebot

from src.main.resources import config


def get_token():
    logging.info("Attempting to retrieve the bot token")
    try:
        # check bot token
        if not config.token:
            raise ValueError("The token is not set in the configuration file.")
        # return bot token
        logging.info("Bot token successfully retrieved")
        return config.token
    except Exception as e:
        logging.error(f"Failed to retrieve bot token: {e}")
        raise


def main():
    # add path to config.py to sys.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../resources'))
    # connect bot
    bot = telebot.TeleBot(get_token())
    //bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    # logging settings
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="py_log.log"
    )
    main()

''' Подключаемся к базе
conn = psycopg2.connect(dbname=, host=, user=, password=)
conn.autocommit = True  # устанавливаем актокоммит
print("Connection established")
cursor = conn.cursor()
# Fetch all rows from table
cursor.execute("SELECT * FROM status;")
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print(row)

# Cleanup
conn.commit()
cursor.close()
conn.close()
'''
