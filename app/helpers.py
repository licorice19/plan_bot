from app.models import Chat
from app import chats, bot


async def chat_helper(message) -> Chat:
    chat_id = message.chat.id
    if chat_id not in chats:
        chat = Chat(chat_id)
        chats[chat_id] = chat
    return chats[chat_id]


async def start_handler_helper(message):
    chat: Chat = await chat_helper(message)
    await bot.reply_to(message, 'Используйте /help чтобы получить список команд')


async def plan_handler_helper(message):
    chat = await chat_helper(message)
    msg = message.text
    reply_text = ''
    try:
        new_plan = msg.split()[1]
        chat.plan = new_plan
        reply_text = f"Установлен новый план: {new_plan}"
    except (IndexError):
        reply_text = chat.get_plan()
    except Exception as e:
        reply_text = f"Ошибка: {e}"
    finally:
        await bot.reply_to(message, str(reply_text))


async def default_handler_helper_sum(chat: Chat, beznal=None, nal=None, schet=None, vozvrat=None) -> str:
    """
    Обрабатывает данные о суммах и возвращает текстовый ответ.

    Args:
        chat (Chat): Объект чата.
        beznal: Сумма по безналу.
        nal: Сумма наличными.
        schet: Сумма на счет.
        vozvrat: Сумма возврата.

    Returns:
        str: Текстовый ответ.
    """
    try:
        chat.reset_values()
        if beznal is not None:
            chat.beznal = beznal
        if nal is not None:
            chat.nal = nal
        if schet is not None:
            chat.schet = schet
        if vozvrat is not None:
            chat.vozvrat = vozvrat
        return chat.get_plan()
    except (IndexError, TypeError):
        return "Ошибка форматирования. Пример: безнал+нал 1234+3221"
    except Exception as e:
        return f"Ошибка: {e}"


async def default_handler_helper_amount(chat: Chat, amount) -> str:
    """
    Обрабатывает общую сумму и возвращает текстовый ответ.

    Args:
        chat (Chat): Объект чата.
        amount: Общая сумма.

    Returns:
        str: Текстовый ответ или False в случае ошибки.
    """
    try:
        chat.reset_values()
        chat.amount = amount
        return chat.get_plan()
    except Exception:
        return False


async def default_handler_helper(message):
    """
    Основная функция обработки сообщения.

    Args:
        message: Объект сообщения.
    """
    chat: Chat = await chat_helper(message)
    msg = message.text
    args = msg.split(' ')
    if len(args) > 1:
        if args[0] == '/r':
            arg = args[1].replace(' ', '').split('-')  # удаляем пробелы из вводимой строки и разбиваем ее по знаку "-"
            vozvrat = None
            if len(arg) > 1:
                summa, vozvrat = arg
                parts = summa.split('+')
            else:
                parts = arg[0].split('+')
    else:
        arg = args[0].replace(' ', '').split('-')  # удаляем пробелы из вводимой строки и разбиваем ее по знаку "-"
        vozvrat = None
        if len(arg) > 1:
            summa, vozvrat = arg
            parts = summa.split('+')
        else:
            parts = arg[0].split('+')

    beznal = None
    nal = None
    schet = None

    # Парсинг частей сообщения
    if len(parts) == 2:
        beznal, nal = parts
    elif len(parts) == 3:
        beznal, nal, schet = parts
    elif len(parts) == 4:
        beznal, nal, schet, vozvrat = parts

    # Вызов соответствующей функции обработки
    if beznal is not None and nal is not None:
        reply_text = await default_handler_helper_sum(chat, beznal=beznal, nal=nal, schet=schet, vozvrat=vozvrat)
        await bot.reply_to(message, reply_text)
    else:
        reply_text = await default_handler_helper_amount(chat, parts[0])
        if reply_text:
            await bot.reply_to(message, reply_text)


async def help_handler_helper(message):
    chat: Chat = await chat_helper(message)
    reply_text = '```Пример\nВводите суммы безнал, нал и счет при наличии вычитайте возврат при наличии: [безнал]+[нал]+[счет]-[возврат] 5585\+1337\+3000\-1000 нал = n, безнал = b, счета = c, возврат =  v\nn\+b\nn\+b\+c\nn\+b\+c\+v\nn\+b\-v\nn\+b\+c\-v```\n```Пример\nЕсли все подсчитано, то общую сумму\n8922```\n\n/r \[безнал\]\+\[нал\]\+\[счета\]\+\[возврат\] \- расчет выручки в группe\n/plan \[сумма\] \- Установить план \n/plan \- Посмотреть сводку по плану\n/reset \- Cброс выручки и плана\n/help \- Помощь по командам\. \nВ группе бот работает через реплай или команду /r'
    await bot.reply_to(message, reply_text, parse_mode='MarkdownV2')


async def reset_handler_helper(message):
    chat: Chat = await chat_helper(message)
    chat.reset_values(True)
    reply_text = "Все значения сброшены"
    await bot.reply_to(message, reply_text)
