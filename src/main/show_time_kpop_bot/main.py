import logging
import os
import sys
import telebot

from src.main.resources import config
from src.main.show_time_kpop_bot import handlers


def get_token():
    logging.info("Attempting to retrieve the bot token")
    try:
        # check bot token
        if not config.token or not config.admins:
            raise ValueError("The token ar admins are not set in the configuration file.")
        # return bot token
        logging.info("Bot token and admins list successfully retrieved")
        return config.token, config.admins
    except Exception as e:
        logging.error(f"Failed to retrieve bot token or admins list: {e}")
        raise


def main():
    # connect bot
    token, admins_list = get_token()
    handlers.start_bot(token, admins_list)


if __name__ == "__main__":
    # logging settings
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename="py_log.log"
    )
    main()
    # add path to config.py to sys.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../resources'))