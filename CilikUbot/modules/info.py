import os
import json
import requests
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from CilikUbot.modules.sql_helper.globals import gvarstatus
from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from CilikUbot.utils import edit_delete, edit_or_reply, cilik_cmd
from datetime import datetime
from math import sqrt

from emoji import emojize
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import (
    GetFullChannelRequest,
    GetParticipantsRequest,
)
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
    MessageActionChannelMigrateFrom,
)
from telethon.utils import get_input_location


@cilik_cmd(pattern="limit(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest("@SpamBot"))
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        await xx.edit(f"~ {response.message.message}")
        
        
@cilik_cmd(pattern="info(?: |$)(.*)")
async def who(event):
    xx = await edit_or_reply(event, "`Mengambil Informasi Pengguna Ini...`")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    if replied_user is None:
        return await xx.edit(
            "**itu admin anonim, selamat mencoba cari tahu yang mana!**"
        )
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await xx.edit("**Saya Tidak Mendapatkan Informasi Apapun.**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode=r"html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await event.delete()
    except TypeError:
        await xx.edit(caption, parse_mode=r"html")


async def get_user(event):
    """Get the user from argument or replied message."""
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        if previous_message.sender_id is None and not event.is_private:
            return None
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            return await event.edit(str(err))

    return replied_user


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = (
        "Orang tersebut membutuhkan bantuan untuk mengupload gambar profil."
    )
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, _ = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Tidak Dapat Mengambil DC ID!"
        str(e)
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TEMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "") if first_name else ("Tidak Ada Nama Depan")
    )
    last_name = (
        last_name.replace("\u2060", "") if last_name else ("Tidak Ada Nama Belakang")
    )
    username = f"@{username}" if username else ("Tidak Menggunakan Username")
    user_bio = "Tidak Menggunakan Bio" if not user_bio else user_bio

    caption = "<b>INFORMASI PENGGUNA :</b>\n\n"
    caption += f"Nama Depan : {first_name}\n"
    caption += f"Nama Belakang : {last_name}\n"
    caption += f"Username : {username}\n"
    caption += f"Data Centre ID : {dc_id}\n"
    caption += f"Total Foto Profil : {replied_user_profile_photos_count}\n"
    caption += f"Apakah Bot : {is_bot}\n"
    caption += f"Apakah Dibatasi : {restricted}\n"
    caption += f"Diverifikasi Oleh Telegram : {verified}\n"
    caption += f"User ID : <code>{user_id}</code>\n\n"
    caption += f"Bio : <code>{user_bio}</code>\n\n"
    caption += f"Group yang sama Dengan Pengguna Ini : {common_chat}\n"
    caption += "Link Permanen Ke Profil : "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'

    return photo, caption


@cilik_cmd(pattern="cinfo(?: |$)(.*)")
async def info(event):
    xx = await edit_or_reply(event, "`Menganalisis Obrolan Ini...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await xx.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await xx.edit("**Terjadi Kesalah Yang Tidak Terduga.**")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await edit_or_reply(event, "`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await edit_or_reply(
                event, "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await edit_or_reply(event, "`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await edit_or_reply(event, "`Invalid channel/group`")
            return None
    return chat_info


async def fetch_info(chat, event):
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = (
        chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    )
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(
            GetHistoryRequest(
                peer=chat_obj_info.id,
                offset_id=0,
                offset_date=datetime(2010, 1, 1),
                add_offset=-1,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    first_msg_valid = bool(
        msg_info and msg_info.messages and msg_info.messages[0].id == 1
    )
    creator_valid = bool(first_msg_valid and msg_info.users)
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = (
        msg_info.users[0].first_name
        if creator_valid and msg_info.users[0].first_name is not None
        else "Akun Terhapus"
    )
    creator_username = (
        msg_info.users[0].username
        if creator_valid and msg_info.users[0].username is not None
        else None
    )
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = (
        msg_info.messages[0].action.title
        if first_msg_valid
        and isinstance(msg_info.messages[0].action, MessageActionChannelMigrateFrom)
        and msg_info.messages[0].action.title != chat_title
        else None
    )
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        str(e)

    description = chat.full_chat.about
    members = (
        chat.full_chat.participants_count
        if hasattr(chat.full_chat, "participants_count")
        else chat_obj_info.participants_count
    )
    admins = (
        chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    )
    banned_users = (
        chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    )
    restrcited_users = (
        chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    )
    members_online = (
        chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    )
    group_stickers = (
        chat.full_chat.stickerset.title
        if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset
        else None
    )
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = (
        chat.full_chat.read_inbox_max_id
        if hasattr(chat.full_chat, "read_inbox_max_id")
        else None
    )
    messages_sent_alt = (
        chat.full_chat.read_outbox_max_id
        if hasattr(chat.full_chat, "read_outbox_max_id")
        else None
    )
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup
        else "Tidak"
    )
    slowmode = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled
        else "Tidak"
    )
    slowmode_time = (
        chat.full_chat.slowmode_seconds
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled
        else None
    )
    restricted = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted
        else "Tidak"
    )
    verified = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "verified") and chat_obj_info.verified
        else "Tidak"
    )
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None

    if admins is None:
        try:
            participants_admins = await event.client(
                GetParticipantsRequest(
                    channel=chat.full_chat.id,
                    filter=ChannelParticipantsAdmins(),
                    offset=0,
                    limit=0,
                    hash=0,
                )
            )
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for _ in bots_list:
            bots += 1

    caption = "<b>INFORMASI OBROLAN:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} Nama: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Nama Lama: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} Type: Publik\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} type: Privasi\n"
    if creator_username is not None:
        caption += f"Pembuat: {creator_username}\n"
    elif creator_valid:
        caption += (
            f'Pembuat: <a href="tg://user?id={creator_id}">{creator_firstname}</a>\n'
        )
    if created is not None:
        caption += f"Informasi Pembuatan: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"Informasi Pembuatan: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1 + sqrt(1 + 7 * exp_count / 14)) / 2)
        caption += f"{chat_type} Level: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"Pesan Yang Dapat Dilihat: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Pesan Dikirim: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Pesan Dikirim: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"Member: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Admin: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Bot: <code>{bots}</code>\n"
    if members_online:
        caption += f"Sedang Online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"Pengguna Yang Dibatasi: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"Banned Pengguna: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f'{chat_type} Sticker: <a href="t.me/addstickers/{chat.full_chat.stickerset.short_name}">{group_stickers}</a>\n'
    caption += "\n"
    if not broadcast:
        caption += f"Mode Slow: {slowmode}"
        if (
            hasattr(chat_obj_info, "slowmode_enabled")
            and chat_obj_info.slowmode_enabled
        ):
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
        caption += f"Supergrup: {supergroup}\n\n"
    if hasattr(chat_obj_info, "Terbatas"):
        caption += f"Terbatas: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> Platform: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> Alasan: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Teks: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += "Scam: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Di Verifikasi Oleh Telegram: {verified}\n\n"
    if description:
        caption += f"Deskripsi: \n<code>{description}</code>\n"
    return caption
  
  
@cilik_cmd(pattern="bots(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bot Di Group Ini:** \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = "Bot Dalam {} Group: \n".format(input_str)
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            await edit_or_reply(event, str(e))
            return None
    try:
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsBots
        ):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n 👑 [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
            else:
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await edit_or_reply(event, mentions)
    
  
@cilik_cmd(pattern="adzan(?:\s|$)([\s\S]*)")
async def get_adzan(adzan):
    "Shows you the Islamic prayer times of the given city name"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus("WEATHER_DEFCITY") or "Jakarta" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"**Tidak Dapat Menemukan Kota** `{LOCATION}`", 120
        )
    result = json.loads(request.text)
    catresult = f"<b>Jadwal Shalat Hari Ini:</b>\
            \n<b>📆 Tanggal </b><code>{result['items'][0]['date_for']}</code>\
            \n<b>📍 Kota</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
            \n\n<b>Terbit  : </b><code>{result['items'][0]['shurooq']}</code>\
            \n<b>Subuh : </b><code>{result['items'][0]['fajr']}</code>\
            \n<b>Zuhur  : </b><code>{result['items'][0]['dhuhr']}</code>\
            \n<b>Ashar  : </b><code>{result['items'][0]['asr']}</code>\
            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
            \n<b>Isya : </b><code>{result['items'][0]['isha']}</code>\
    "
    await edit_or_reply(adzan, catresult, "html")

    
CMD_HELP.update(
    {
        "Info": f"**➢ Plugin : **`Information`\
        \n\n **ᴄᴍᴅ :** `{cmd}limit`\
        \n └⋟ Info Akun mu di @SpamBot\
        \n\n **ᴄᴍᴅ :** `{cmd}info <username> or Reply Chat`\
        \n └⋟ Mendapatkan Informasi Pengguna.\
        \n\n **ᴄᴍᴅ :** `{cmd}cinfo` [opsional: <reply/tag/chat id/invite link>]\
        \n └⋟ Mendapatkan info obrolan. Beberapa info mungkin dibatasi karena izin yang hilang.\
        \n\n **ᴄᴍᴅ :** `{cmd}bots`\
        \n └⋟ Dapatkan List Bot dalam grup chat.\
        \n\n **ᴄᴍᴅ :** `{cmd}adzan` <nama kota>\
        \n └⋟ Menunjukkan waktu jadwal sholat dari kota yang diberikan\
    "
    }
)  
