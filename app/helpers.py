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


async def default_handler_helper_sum(rev1, rev2, chat: Chat) -> str:
    try:
        chat.beznal = rev1
        chat.nal = rev2
        reply_text = chat.get_plan()
    except (IndexError):
        reply_text = f"Ошибка форматирования. Пример: безнал+нал 1234+3221"
    except Exception as e:
        reply_text = f"Ошибка: {e}"
    finally:
        return reply_text


async def default_handler_helper_amount(amount, chat: Chat) -> str:
    try:
        chat.amount = amount
        reply_text = chat.get_plan()
        return reply_text
    except Exception:
        return False


async def default_handler_helper(message):
    chat: Chat = await chat_helper(message)
    msg = message.text
    rev = msg.split('+')

    if len(rev) > 1:
        reply_text = await default_handler_helper_sum(rev[0], rev[1], chat)
        await bot.reply_to(message, str(reply_text))
    else:
        reply_text = await default_handler_helper_amount(rev[0], chat)
        if reply_text:
            await bot.reply_to(message, str(reply_text))


async def help_handler_helper(message):
    chat: Chat = await chat_helper(message)
    reply_text = 'Вводите безнал и нал: ```Пример\n[безнал]+[нал] \n5585+1337```\nЕсли все подсчитано, то общую сумму ```Пример\n6922```\n\n/plan \[сумма\] \- Установить план \n/plan \- Посмотреть сводку по плану \n/help \- Помощь по командам'
    await bot.reply_to(message, reply_text, parse_mode='MarkdownV2')
