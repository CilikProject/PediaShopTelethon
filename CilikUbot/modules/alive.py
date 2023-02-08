import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version
from shutil import which

import psutil
from pytgcalls import __version__ as pytgcalls
from telethon import __version__, version

from userbot import ALIVE_EMOJI, ALIVE_LOGO, ALIVE_NAME, BOT_VER, CHANNEL
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, GROUP, StartTime, bot
from userbot.utils import bash, edit_or_reply, cilik_cmd

from .ping import get_readable_time

@cilik_cmd(pattern="(?:alive|on)\s?(.)?")
async def amireallyalive(alive):
    logo = "https://telegra.ph/file/db8f3a0d1002be7ab2ed2.png"  
    user = await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    output = (
        f"**[PediaShop- Spambot](https://t.me/{GROUP}) is Up and Running.**\n\n"
        f"**I am Alive**\n\n"
        f"⚡️ **Master :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"⚡️ **Version :** `{BOT_VER}` \n"
        f"⚡️ **Python :** `{python_version()}` \n"
        f"⚡️ **Telethon :** `{version.__version__}` \n"
        f"⚡️ **BotUptime :** `{uptime}` \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={user.id})**"
    )
    if ALIVE_LOGO:
        try:
            logo = logo
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
        except BaseException:
            await alive.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
    else:
        await edit_or_reply(alive, output)
        
        
CMD_HELP.update(
    {
        "Gcast": f"**➢ Plugin : **`alive`\
        \n\n **ᴄᴍᴅ :** `{cmd}alive`\
        \n └⋟ Untuk mengecek sistem bot\
    "
    }
)        
