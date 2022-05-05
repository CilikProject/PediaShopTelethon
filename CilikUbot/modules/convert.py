# cilik - ubot v2

import asyncio
import io
import math
import random
import urllib.request
from os import remove

import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from telethon import events
from telethon.errors import PackShortNameOccupiedError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputStickerSetID,
    MessageMediaPhoto,
)
from telethon.utils import get_input_document

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import S_PACK_NAME as packcustom
from userbot import tgbot, user
from userbot.modules.sql_helper.globals import addgvar, gvarstatus

import io
import os

from PIL import Image

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP
from CilikUbot.utils import cilik_cmd, edit_delete, edit_or_reply


@cilik_cmd(pattern="mtoi$")
async def cevir(event):
    rep_msg = await event.get_reply_message()
    if not event.is_reply or not rep_msg.sticker:
        await edit_delete(event, "**Reply to sticker**")
        return
    xxnx = await edit_or_reply(event, "`Processing...`")
    foto = io.BytesIO()
    foto = await event.client.download_media(rep_msg.sticker, foto)
    im = Image.open(foto).convert("RGB")
    im.save("sticker.png", "png")
    await event.client.send_file(
        event.chat_id,
        "sticker.png",
        reply_to=rep_msg,
    )
    await xxnx.delete()
    os.remove("sticker.png")


@cilik_cmd(pattern="mtos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(
            event, "sir this is not a image message reply to image message"
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_delete(event, "sir, This is not a image ")
        return
    chat = "@buildstickerbot"
    xx = await event.reply("`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164977173)
            )
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        if response.text.startswith("Hi!"):
            await xx.edit(
                "Can you kindly disable your forward privacy settings for good?"
            )
        else:
            await xx.delete()
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


CMD_HELP.update(
    {
        "Converter": f"**➢ Plugin : **`Converter`\
        \n\n **ᴄᴍᴅ :** `{cmd}mtos`\
        \n └⋟ Untuk Mengconvert sticker ke foto\
        \n\n **ᴄᴍᴅ :** `{cmd}mtoi`\
        \n └⋟ Untuk Mengconvert foto ke sticker\
    "
    }
)
