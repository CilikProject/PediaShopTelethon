# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
# cilik - ubot v2

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, CILIK2, CILIK3, CILIK4, CILIK5, CILIK6, CILIK7, CILIK8, CILIK9, CILIK10):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if CILIK2 is not None:
            id2 = await CILIK2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if CILIK3 is not None:
            id3 = await CILIK3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if CILIK4 is not None:
            id4 = await CILIK4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if CILIK5 is not None:
            id5 = await CILIK5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    try:
        if CILIK6 is not None:
            id6 = await CILIK6.get_me()
            user_ids.append(id6.id)
    except BaseException:
        pass

    try:
        if CILIK7 is not None:
            id7 = await CILIK7.get_me()
            user_ids.append(id7.id)
    except BaseException:
        pass

    try:
        if CILIK8 is not None:
            id8 = await CILIK8.get_me()
            user_ids.append(id8.id)
    except BaseException:
        pass

    try:
        if CILIK9 is not None:
            id9 = await CILIK9.get_me()
            user_ids.append(id9.id)
    except BaseException:
        pass

    try:
        if CILIK10 is not None:
            id10 = await CILIK10.get_me()
            user_ids.append(id10.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTc4NDYwNjU1Ng==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        CILIK_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        CILIK_USER = client.first_name
    cilik_mention = f"[{CILIK_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, CILIK_USER, cilik_mention
