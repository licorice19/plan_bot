from telebot.async_telebot import AsyncTeleBot
from config import token, debug, dsn
from asyncio import run
import logging
import sentry_sdk

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="errors.log", filemode="w")

sentry_sdk.init(
    dsn=dsn,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

try:
    bot = AsyncTeleBot(token)

    chats = {}

    from app import commands, models, errors, helpers, validators
    from telebot.types import Message

    errors.error_init_handler_token_value(token)

    run(bot.polling(), debug=debug)
except Exception as e:
    logging.critical(f'Critical error', exc_info=True)