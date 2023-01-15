import time
from datetime import datetime
from CilikUbot import StartTime
from CilikUbot.utils import cilik_cmd

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
  
  
@cilik_cmd(pattern="ping$")
async def _(pang):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pang.reply(
        f"**Pong!** \n`%sms`" % (duration)
    ) 


@cilik_cmd(pattern="ubot$")
async def _(yanto):
    await yanto.reply(
        "**Wusshh YantoUbot Is Alive Masseh Angjay🗿:**\n"
        "    **dc_id:** `Jepang Barat`\n"
        "    **ping_dc:** `1000ms`\n"
        "    **peer_users:** `999999 users`\n"
        "    **peer_groups:** `full groups`\n"
        "    **yanto_uptime:** `seabad`\n"
        "    **waktu yanto vcs:** `2 Jam`\n")


