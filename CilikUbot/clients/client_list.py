# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
# cilik - ubot v2

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, CILIK2, CILIK3, CILIK4, CILIK5, CILIK6, CILIK7, CILIK8, CILIK9, CILIK10, CILIK11, CILIK12, CILIK13, CILIK14, CILIK15, CILIK16, CILIK17, CILIK18, CILIK19, CILIK20):
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

    try:
        if CILIK11 is not None:
            id11 = await CILIK11.get_me()
            user_ids.append(id11.id)
    except BaseException:
        pass

    try:
        if CILIK12 is not None:
            id12 = await CILIK12.get_me()
            user_ids.append(id12.id)
    except BaseException:
        pass

    try:
        if CILIK13 is not None:
            id13 = await CILIK13.get_me()
            user_ids.append(id13.id)
    except BaseException:
        pass

    try:
        if CILIK14 is not None:
            id14 = await CILIK14.get_me()
            user_ids.append(id14.id)
    except BaseException:
        pass

    try:
        if CILIK15 is not None:
            id15 = await CILIK15.get_me()
            user_ids.append(id15.id)
    except BaseException:
        pass

    try:
        if CILIK16 is not None:
            id16 = await CILIK16.get_me()
            user_ids.append(id16.id)
    except BaseException:
        pass

    try:
        if CILIK17 is not None:
            id17 = await CILIK17.get_me()
            user_ids.append(id17.id)
    except BaseException:
        pass

    try:
        if CILIK18 is not None:
            id18 = await CILIK18.get_me()
            user_ids.append(id18.id)
    except BaseException:
        pass

    try:
        if CILIK19 is not None:
            id19 = await CILIK19.get_me()
            user_ids.append(id19.id)
    except BaseException:
        pass

    try:
        if CILIK20 is not None:
            id20 = await CILIK20.get_me()
            user_ids.append(id20.id)
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
