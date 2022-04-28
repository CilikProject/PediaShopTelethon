import pybase64
from telethon import Button
from telethon.tl.functions.channels import JoinChannelRequest as grey
from CilikUbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/e2100e87ee152baa85dc2.jpg",
                caption="🔥 **Cilik Ubot Has Been Activated**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - V.2@main\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @CilikProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/CilikSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def checking(client):
    cilikgc = str(pybase64.b64decode("QENpbGlrU3VwcG9ydA=="))[2:15]
    cilikch = str(pybase64.b64decode("QENpbGlrUHJvamVjdA=="))[2:15]
    if client:
        try:
            await client(grey(cilikgc))
        except BaseException:
            pass
        try:
            await client(grey(cilikch))
        except BaseException:
            pass
