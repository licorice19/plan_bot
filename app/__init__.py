from logging.handlers import RotatingFileHandler
from telebot.async_telebot import AsyncTeleBot
from config import token, debug
from asyncio import run
import os
import logging
import sentry_sdk

if not os.path.exists('logs'):
            os.mkdir('logs')
file_handler = RotatingFileHandler(
    'logs/bot.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                            '[in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)

logger = logging.Logger('bot_logger', logging.INFO)

logging.Logger.addHandler(logger, file_handler)
try:
    bot = AsyncTeleBot(token)

    chats = {}

    from app import commands, models, errors, helpers, validators
    from telebot.types import Message

    errors.error_init_handler_token_value(token)
    run(bot.polling(), debug=debug)
except Exception as e:
    logging.critical(f'Critical error', exc_info=True)
