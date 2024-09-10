from app import bot, logging, debug
from app.helpers import start_handler_helper, plan_handler_helper, default_handler_helper, help_handler_helper, reset_handler_helper

@bot.message_handler(commands=["start"])
async def start_handler(message):
    try:
        await start_handler_helper(message)
        # if debug:
        #     logging.info('Success calling start_handler')
    except Exception:
        logging.error(f'Something wrong in "start_handler": ', exc_info=True)
    

@bot.message_handler(commands=["plan"])
async def plan_handler(message):
    try:
        await plan_handler_helper(message)
        # if debug:
        #     logging.info('Success calling plan_handler')
    except Exception:
        logging.error(f'Something wrong in "plan_handler": ', exc_info=True)

@bot.message_handler(commands=["help"])
async def help_handler(message):
    try:
        await help_handler_helper(message)
        # if debug:
        #     logging.info('Success calling help_handler')
    except Exception:
        logging.error(f'Something wrong in "help_handler": ', exc_info=True)

@bot.message_handler(commands=["r"])
async def reply_handler(message):
    try:
        await default_handler_helper(message)
        # if debug:
        #     logging.info('Success calling reply_handler')
    except Exception:
        logging.error(f'Something wrong in "reply_handler": ', exc_info=True)

@bot.message_handler(commands=["reset"])
async def reset_handler(message):
    try:
        await reset_handler_helper(message)
        # if debug:
        #     logging.info('Success calling reset_handler')
    except Exception:
        logging.error(f'Something wrong in "reset_handler": ', exc_info=True)

@bot.message_handler()
async def default_handler(message):
    try:
        await default_handler_helper(message)
        # if debug:
        #     logging.info('Success calling default_handler')
    except Exception:
        logging.error(f'Something wrong in "default_handler": ', exc_info=True)