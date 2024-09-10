from app import logging

def error_init_handler_token_value(token: str) -> Exception:
    try:
        if token == "Default":
            logging.critical(f"Invalid bot token: {token}")
            raise ValueError("Измените токен бота в config.ini. Получить токен https://t.me/BotFather")
        else:
            logging.info(f'Bot is launching...')
    except Exception:
        logging.critical(f'Invalid bot token: ', exc_info=True)
        raise ValueError("Измените токен бота в config.ini. Получить токен https://t.me/BotFather")

def error_value_int_error(integer, attributeName):
    try:
        return int(integer)
    except Exception:
        logging.error(f"Invalid {attributeName}: {integer} is not an integer.", exc_info=True)
    
def error_value_float_error(float_int, attributeName):
    try:
        return round(float(float_int), 2)
    except Exception:
        logging.error(f"Invalid {attributeName}: {float_int} is not an integer.", exc_info=True)