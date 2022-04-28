# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from pytgcalls import idle
from telethon import version

from CilikUbot import BOT_TOKEN
from CilikUbot import BOT_VER as ubotversion
from CilikUbot import BOTLOG_CHATID, LOGS, LOOP, bot
from CilikUbot.clients import cilik_userbot_on, multicilik
from CilikUbot.core.git import git
from CilikUbot.modules import ALL_MODULES
from CilikUbot.utils import autobot, autopilot

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"CilikUbot.modules.{module_name}")
    client = multicilik()
    total = 10 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__}")
    LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")
    LOGS.info(f"Cilik-Ubot Version - {ubotversion} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(cilik_userbot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
