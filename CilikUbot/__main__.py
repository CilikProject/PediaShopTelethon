# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from CilikUbot import (
    BOT_VER,
    LOGS,
    bot,
)
from CilikUbot.modules import ALL_MODULES
from CilikUbot.clients import cilik_userbot_on, multicilik
from CilikUbot.core.git import git

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"CilikUbot.modules.{module_name}")
    client = multicilik()
    total = 20 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
    LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)



bot.loop.run_until_complete(cilik_userbot_on())
LOGS.info(
    f"Jika Anda Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/CilikSupport")
LOGS.info(
    f"✨Cilik-Ubot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
