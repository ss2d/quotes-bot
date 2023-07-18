from os import environ

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()


class Telegram:
    token = environ.get('TOKEN')
    bot: Bot = None
    username: str = None

    message_is_not_modified = 'Bad Request: message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message'


class DB:
    host = environ.get('DB_HOST')
    port = int(environ.get('DB_PORT'))
    user = environ.get('DB_USER')
    password = environ.get('DB_PASSWORD')
    db_name = environ.get('DB_NAME')
