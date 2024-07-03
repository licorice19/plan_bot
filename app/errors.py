def error_init_handler_token_value(token: str) -> Exception:
    if token == "Default":
        raise ValueError("Измените токен бота в config.ini. Получить токен https://t.me/BotFather")

def error_value_int_error(integer, attributeName):
    try:
        return int(integer)
    except Exception:
        raise TypeError(f"{attributeName} должен быть числом")
    
def error_value_float_error(float_int, attributeName):
    try:
        return round(float(float_int), 2)
    except Exception:
        raise TypeError(f"{attributeName} должен быть числом с плавающей запятой")