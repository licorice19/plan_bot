from app import bot
from app.helpers import start_handler_helper, plan_handler_helper, default_handler_helper, help_handler_helper

@bot.message_handler(commands=["start"])
async def start_handler(message):
    await start_handler_helper(message)

@bot.message_handler(commands=["plan"])
async def plan_handler(message):
    await plan_handler_helper(message)

@bot.message_handler(commands=["help"])
async def help_handler(message):
    await help_handler_helper(message)

@bot.message_handler()
async def default_handler(message):
    await default_handler_helper(message)