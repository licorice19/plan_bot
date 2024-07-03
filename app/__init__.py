from telebot.async_telebot import AsyncTeleBot
from config import token, debug
from asyncio import run


bot = AsyncTeleBot(token)

chats = {}

from app import commands, models, errors, helpers, validators
from telebot.types import Message

errors.error_init_handler_token_value(token)

run(bot.polling(), debug=debug)