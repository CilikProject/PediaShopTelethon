from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from CilikUbot import bot
from CilikUbot.modules.sql_helper.globals import gvarstatus
from CilikUbot import bot

import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery

from CilikUbot import bot
from CilikUbot.modules.sql_helper.globals import gvarstatus


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        user = await bot.get_me() or await bot.get_sender()
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
        else:
            HELP_TEXT = (
                gvarstatus("HELP_TEXT")
                or f"Hanya bos saya yang dapat Mengakses Ini!!\nSilahkan Buat UserBot Anda sendiri."
            )
            await c_q.answer(
                HELP_TEXT,
                alert=True,
            )

    return wrapper
