# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
# cilik - ubot v2

import sys

from telethon.utils import get_peer_id

from CilikUbot import BOT_TOKEN
from CilikUbot import BOT_VER as version
from CilikUbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    CILIK2,
    CILIK3,
    CILIK4,
    CILIK5,
    CILIK6,
    CILIK7,
    CILIK8,
    CILIK9,
    CILIK10,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,  
    STRING_SESSION,
    blacklistcilik,
    bot,
    call_py,
    tgbot,
)
from CilikUbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nCilik-Ubot v{}, Copyright © 2021-2022 PayXr <https://github.com/grey423>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCilik-Ubot v{}, Copyright © 2021-2022 PayXr <https://github.com/grey423>"


async def cilik_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multicilik():
    if 1784606556 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001687155877 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1784606556 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(cilik_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            CILIK2.start()
            LOOP.run_until_complete(cilik_client(CILIK2))
            user = CILIK2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            CILIK3.start()
            LOOP.run_until_complete(cilik_client(CILIK3))
            user = CILIK3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            CILIK4.start()
            LOOP.run_until_complete(cilik_client(CILIK4))
            user = CILIK4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            CILIK5.start()
            LOOP.run_until_complete(cilik_client(CILIK5))
            user = CILIK5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_6:
        try:
            CILIK6.start()
            LOOP.run_until_complete(cilik_client(CILIK6))
            user = CILIK6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            CILIK7.start()
            LOOP.run_until_complete(cilik_client(CILIK7))
            user = CILIK7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            CILIK8.start()
            LOOP.run_until_complete(cilik_client(CILIK8))
            user = CILIK8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            CILIK9.start()
            LOOP.run_until_complete(cilik_client(CILIK9))
            user = CILIK9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))
            
    if STRING_10:
        try:
            CILIK10.start()
            LOOP.run_until_complete(cilik_client(CILIK10))
            user = CILIK10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistcilik:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))            

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1 
    if not STRING_10:
        failed += 1         
    return failed
