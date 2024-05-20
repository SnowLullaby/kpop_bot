import psycopg2
import logging
from src.main.resources import config


def new_user(user_id):
    try:
        conn, cursor = connection()
        cursor.execute("INSERT INTO users(name) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM users WHERE name = %s);",
                       (str(user_id), str(user_id)))
        logging.info("User %s added", str(user_id))
        close(conn, cursor)
    except Exception as e:
        logging.error(f"SQL error: {e}")


def connection():
    logging.info("Attempting to retrieve the database connection settings")
    try:
        # check settings
        if not config.dbname or not config.host or not config.user or not config.password:
            raise ValueError("The settings is not set in the configuration file.")
    except Exception as e:
        logging.error(f"Failed to retrieve db settings: {e}")
        raise

    try:
        # connecting to db
        conn = psycopg2.connect(dbname=config.dbname, host=config.host, user=config.user, password=config.password)
        conn.autocommit = True  # set autocommit
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        logging.error(f"Connection failed: {e}")
        raise


def close(conn, cursor):
    cursor.close()
    conn.close()
