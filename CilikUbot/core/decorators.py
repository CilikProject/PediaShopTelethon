import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from CilikUbot import bot


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        user = await bot.get_sender()
        uid = user.id
        if c_q.query.user_id and (
            c_q.query.user_id == uid 
        ):
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass

    return wrapper
