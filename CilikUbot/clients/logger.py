import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from CilikUbot import BOT_VER as version
from CilikUbot import BOTLOG_CHATID
from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import bot, tgbot
from CilikUbot.utils.events import checking

MSG_ON = """
❏  - ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼━━━╍━━━━━┅╾
├▹ Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {}
├▹ Kᴇᴛɪᴋ {}alive Uɴᴛᴜᴋ Mᴇɴɢᴇᴄᴇᴋ Bᴏᴛ
╰╼┅━━━━━━━━┅╾
"""


async def cilik_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            CilikUBOT = await tgbot.get_me()
            BOT_USERNAME = CilikUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            CilikUBOT = await tgbot.get_me()
            BOT_USERNAME = CilikUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "Assɪsᴛᴀɴᴛ"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, cmd),
                )
    except BaseException:
        pass
