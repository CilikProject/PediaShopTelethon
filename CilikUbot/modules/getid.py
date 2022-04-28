from telethon.utils import pack_bot_file_id

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, LOGS
from CilikUbot.utils import edit_delete, cilik_cmd
from CilikUbot.utils.logger import logging

LOGS = logging.getLogger(__name__)


@cilik_cmd(pattern="(get_id|id)(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await event.reply(
                    f"User ID {input_str} adalah `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await event.reply(
                        f"ID {p.title} adalah `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await event.reply("`Berikan Username atau Reply ke pesan pengguna`")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.reply(
                "**💬 Message ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`\n**💎 Bot API File ID:** `{}`".format(
                    str(r_msg.id),
                    str(r_msg.sender_id),
                    bot_api_file_id,
                ),
            )

        else:
            await event.reply(
                "**👥 Chat ID:** `{}`\n**💬 Message ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.id), str(r_msg.sender_id)
                ),
            )

    else:
        await event.reply(f"**👥 Chat ID: **`{event.chat_id}`")


CMD_HELP.update(
    {
        "Get_Id": f"**➢ Plugin : **`Get_Id`\
        \n\n **ᴄᴍᴅ :** `{cmd}id` <username/reply>\
        \n └⋟ Untuk Mengambil Chat ID obrolan saat ini\
        \n\n **ᴄᴍᴅ :** `{cmd}userid` <username/reply>\
        \n └⋟ Untuk Mengambil ID & Username obrolan saat ini\
    "
    }
)
