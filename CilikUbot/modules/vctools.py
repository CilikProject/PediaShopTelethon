import asyncio

from pytgcalls.exceptions import NotConnectedError

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, bot
from CilikUbot.utils import cilik_cmd, edit_or_delete as eod, edit_or_delete as eor
from CilikUbot.events import register
from CilikUbot.utils.pytgcalls import Cilik, CLIENTS, VIDEO_ON


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@cilik_cmd(pattern="startvc$", group_only=True)
async def start_voice(c):
    xnxx = await eor(c, "Procesing...")
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(xnxx, "Sorry {} are not admin".format(me.first_name))
        return
    try:
        Xd = Cilik(c.chat_id)
        await Xd.make_vc_active()
        await xnxx.edit("Voicechat started...")
    except Exception as ex:
        await eod(xnxx, "Sorry {} are not admin".format(ex))


@cilik_cmd(pattern="stopvc$", group_only=True)
async def stop_voice(c):
    yins = await eor(c, "Procesing...")
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(yins, "Sorry {} are not admin".format(me.first_name))
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await yins.edit("Voicechat stoped...")
    except Exception as ex:
        await eod(yins, "Error: {}".format(ex))


@cilik_cmd(pattern="vcinvite", group_only=True)
async def _(c):
    xxnx = await eor(c, "Inviting members to voice chat...")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botyins = list(user_list(users, 6))
    for p in botyins:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit("{} Successful people are invited to VCG".format(z))


@cilik_cmd(pattern="vctitle(?: |$)(.*)", group_only=True)
async def change_title(e):
    ayin = await eor(e, "Procesing..")
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await eod(ayin, "Please Enter the Group Voice Chat Title.")

    if not admin and not creator:
        await eod(ayin, "Sorry {} are not admin".format(me.first_name))
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await ayin.edit("Successfully Changed VCG Title To {}".format(title))
    except Exception as ex:
        await eod(ayin, "Error: {}".format(ex))


@cilik_cmd(pattern="joinvc(?: |$)(.*)", group_only=True)
async def _(event):
    sender = await event.get_sender()
    yins = await event.client.get_me()
    if sender.id != yins.id:
        AyiinXd = await event.reply("Procesing...")
    else: 
        AyiinXd = await eor(event, "Procesing...")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(AyiinXd, "Error: {}".format(str(e)))
    else:
        chat = event.chat_id
    Xd = Cilik(chat)
    if not Xd.group_call.is_connected:
        await Xd.group_call.join(chat)
        await AyiinXd.edit("Joined to voicechat...")
        )
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(False)
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(True)



@cilik_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
async def _(event):
    sender = await event.get_sender()
    yins = await event.client.get_me()
    if sender.id != yins.id:
        AyiinXd = await event.reply("Procesing...")
    else: 
        AyiinXd = await eor(event, "Procesing...")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(Ayiin, get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Cilik(chat)
    await Xd.group_call.leave()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await AyiinXd.edit(get_string("levc_1").format(yins.first_name, yins.id, chat))


@cilik_cmd(pattern="rejoin$")
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Cilik(chat)
    try:
        await Xd.group_call.reconnect()
    except NotConnectedError:
        return await event.eor("You are not connected to voice chat yet!")
    await event.eor("Rejoin this voice chat.")


@cilik_cmd(pattern="volume$")
async def volume_setter(event):
    if len(event.text.split()) <= 1:
        return await event.eor("Please specify the volume from 1 to 200!")
    inp = event.text.split()
    if inp[1].startswith(("@","-")):
        chat = inp[1]
        vol = int(inp[2])
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor("Error: {}".format(str(e)))
    elif inp[1].isdigit() and len(inp) == 2:
        vol = int(inp[1])
        chat = event.chat_id
    if vol:
        Xd = Cilik(chat)
        await Xd.group_call.set_my_volume(int(vol))
        if vol > 200:
            vol = 200
        elif vol < 1:
            vol = 1
        return await event.eor("Successfully changed the volume to `{}%`".format(vol))


@cilik_cmd(pattern="skip$")
async def skipper(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor("Error:\n{}".format(str(e)))
    else:
        chat = event.chat_id
    Xd = Cilik(chat, event)
    await Xd.play_from_queue()


CMD_HELP.update(
    {
        "Vctools": f"**⪼ Plugin : **`Vctools`\
        \n\n **ᴄᴍᴅ :** `{cmd}startvc`\
        \n └⋟ Untuk Memulai voice chat group\
        \n\n **ᴄᴍᴅ :** `{cmd}stopvc`\
        \n └⋟ Untuk Memberhentikan voice chat group\
        \n\n **ᴄᴍᴅ :** {cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n └⋟ Untuk Bergabung ke voice chat group\
        \n\n **ᴄᴍᴅ :** `{cmd}rejoin` atau `{cmd}joinvc` <chatid/username gc>\
        \n └⋟ Untuk Bergabung kembali ke voice chat group)\
        \n\n **ᴄᴍᴅ :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n └⋟ Untuk Turun dari voice chat group\
        \n\n **ᴄᴍᴅ :** `{cmd}vctitle` <title vcg>`\
        \n └⋟ Untuk Mengubah title/judul voice chat group\
        \n\n **ᴄᴍᴅ :** `{cmd}vcinvite`\
        \n └⋟ Mengundang Member group ke voice chat group\
    "
    }
)
