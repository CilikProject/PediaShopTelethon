# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

""" Userbot module for System Stats commands """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version
from shutil import which

import psutil
from pytgcalls import __version__ as pytgcalls
from telethon import __version__, version

from CilikUbot import ALIVE_EMOJI, ALIVE_LOGO, ALIVE_NAME, BOT_VER, CHANNEL
from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, GROUP, StartTime, bot
from CilikUbot.utils import bash, edit_or_reply, cilik_cmd

from .ping import get_readable_time

try:
    from carbonnow import Carbon
except ImportError:
    Carbon = None

modules = CMD_HELP
emoji = ALIVE_EMOJI
alive_text = ALIVE_NAME


@cilik_cmd(
    pattern="sysyanto$",
)
async def _(e):
    xxnx = await edit_or_reply(e, "`Processing...`")
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    with open("neo.txt", "r") as neo:
        p = (neo.read()).replace("\n\n", "")
    ok = Carbon(base_url="https://carbonara.vercel.app/api/cook", code=p)
    haa = await ok.memorize("neofetch")
    await e.reply(file=haa)
    await xxnx.delete()
    remove("neo.txt")


@cilik_cmd(pattern=r"yantosystem")
async def psu(event):
    uname = platform.uname()
    softw = "**Informasi Sistem Yanto 👺**\n"
    softw += f"`Sistem Yanto   : {uname.system}`\n"
    softw += f"`Rilis Yanto    : {uname.release}`\n"
    softw += f"`Versi Yanto    : {uname.version}`\n"
    softw += f"`Mesin Yanto   : {uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"`Waktu Hidup Yanto: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**Informasi CPU Yanto 🤖**\n"
    cpuu += "`Physical cores   : " + str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "`Total cores      : " + str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"`Max Frequency    : {cpufreq.max:.2f}Mhz`\n"
    cpuu += f"`Min Frequency    : {cpufreq.min:.2f}Mhz`\n"
    cpuu += f"`Current Frequency: {cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core 🗿**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"`Core {i}  : {percentage}%`\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"`Semua Core: {psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Memori Digunakan Yanto 🎃**\n"
    memm += f"`Total     : {get_size(svmem.total)}`\n"
    memm += f"`Available : {get_size(svmem.available)}`\n"
    memm += f"`Used      : {get_size(svmem.used)}`\n"
    memm += f"`Percentage: {svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bandwith Digunakan Yanto 💩**\n"
    bw += f"`Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"`Download: {get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{softw}\n"
    help_string += f"{cpuu}\n"
    help_string += f"{memm}\n"
    help_string += f"{bw}\n"
    help_string += "**Informasi Mesin**\n"
    help_string += f"`Python {sys.version}`\n"
    help_string += f"`Telethon {__version__}`"
    await edit_or_reply(event, help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@cilik_cmd(pattern="sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await edit_or_reply(sysd, "`" + result + "`")
        except FileNotFoundError:
            await edit_or_reply(sysd, "**Install neofetch Terlebih dahulu!!**")


@cilik_cmd(pattern="(?:spekyanto|on)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    output = (
        f"**[Yanto-Ubot](https://www.yanto.com) is Alive Masseh Angjay 🗿🗿.**\n\n"
        f"🗿 **Mastereh :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"🗿 **Module yanto :** `{len(modules)} Modules` \n"
        f"🗿 **Yanto Versi:** `{BOT_VER}` \n"
        f"🗿 **Piton :** `{python_version()}` \n"
        f"🗿 **Pytgcalls :** `{pytgcalls.__version__}` \n"
        f"🗿 **Telethon :** `{version.__version__}` \n"
        f"🗿 **Bot Hidup :** `{uptime}` \n\n"
        f" **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={user.id})**"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(250)
            await alive.delete()
    else:
        await edit_or_reply(alive, output)


