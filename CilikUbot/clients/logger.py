

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from CilikUbot import BOT_VER as version
from CilikUbot import BOTLOG_CHATID
from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CILIK2, CILIK3, CILIK4, CILIK5, CILIK6, CILIK7, CILIK8, CILIK9, CILIK10, CILIK11, CILIK12, CILIK13, CILIK14, CILIK15, CILIK16, CILIK17, CILIK18, CILIK19, CILIK20, bot, branch, tgbot
from CilikUbot.utils.events import checking

MSG_ON = """
🔥 **PediaShop - Spambot Berhasil Di Aktifkan**
━━━━━━━━━━━━━━━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}ping` **untuk Mengecheck Bot**
━━━━━━━━━━━━━━━━
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
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
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
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK2:
            await checking(CILIK2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK3:
            await checking(CILIK3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK4:
            await checking(CILIK4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK5:
            await checking(CILIK5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK6:
            await checking(CILIK6)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK6.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK7:
            await checking(CILIK7)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK7.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK8:
            await checking(CILIK8)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK8.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK9:
            await checking(CILIK9)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK9.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK10:
            await checking(CILIK10)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK10.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass            
    try:
        if CILIK11:
            await checking(CILIK11)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK11.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass                
    try:
        if CILIK12:
            await checking(CILIK12)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK12.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK13:
            await checking(CILIK13)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK13.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK14:
            await checking(CILIK14)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK14.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK15:
            await checking(CILIK15)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK15.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK16:
            await checking(CILIK16)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK16.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK17:
            await checking(CILIK17)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK17.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK18:
            await checking(CILIK18)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK18.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK19:
            await checking(CILIK19)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK19.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if CILIK20:
            await checking(CILIK20)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await CILIK20.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass            
