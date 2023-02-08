# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, ICON_HELP
from CilikUbot.utils import edit_delete, edit_or_reply, cilik_cmd


@cilik_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1)
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, f"{CMD_HELP[args]}")
        else:
            await edit_delete(event, f"`{args}` **Bukan Nama Modul yang Valid.**")
    else:
        user = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await event.reply(
            "PediaShop 𝗠𝗼𝗱𝘂𝗹𝗲𝘀\n\n"
            "🔮 𝗨𝗯𝗼𝘁: -⋟ `alive` -⋟ `gcast` -⋟ `spam`\n\n" 
            "📮 𝗣𝗿𝗲𝗳𝗶𝘅 -⋟ [ . ]\n"
            "      .help [module_name]\n"
            "      Example: .help gcast\n\n"
            "© __Telethon Version__"

        )
