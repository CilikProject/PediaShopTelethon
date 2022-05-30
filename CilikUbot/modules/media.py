# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# thanks to the owner of X-tra-Telegram for tts fix
#
# Recode by @mrismanaziz
# FROM Man-Userbot
# t.me/SharingUserbot
#
""" Userbot module containing various scrapers. """

import asyncio
import io
import json
import os
import re
import shutil
import time
from asyncio import get_event_loop, sleep
from glob import glob
from re import findall, match

import asyncurban
import barcode
import emoji
import qrcode
import requests
from aiohttp import ClientSession
from barcode.writer import ImageWriter
from bs4 import BeautifulSoup
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from requests import get
from search_engine_parser import BingSearch, GoogleSearch, YahooSearch
from search_engine_parser.core.exceptions import NoResultsOrTrafficError
from telethon.tl.types import (
    DocumentAttributeAudio,
    DocumentAttributeVideo,
    MessageMediaPhoto,
)
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import (
    CMD_HELP,
    LOGS,
    OCR_SPACE_API_KEY,
    REM_BG_API_KEY,
    TEMP_DOWNLOAD_DIRECTORY,
    bot,
)
from CilikUbot.modules.upload_download import get_video_thumb
from CilikUbot.utils import (
    chrome,
    edit_delete,
    edit_or_reply,
    googleimagesdownload,
    cilik_cmd,
    options,
    progress,
)
from CilikUbot.utils.FastTelethon import upload_file

TTS_LANG = "id"
TRT_LANG = "id"


async def ocr_space_file(
    filename, overlay=False, api_key=OCR_SPACE_API_KEY, language="eng"
):

    payload = {
        "isOverlayRequired": overlay,
        "apikey": api_key,
        "language": language,
    }
    with open(filename, "rb") as f:
        r = requests.post(
            "https://api.ocr.space/parse/image",
            files={filename: f},
            data=payload,
        )
    return r.json()


@cilik_cmd(pattern="img (.*)")
async def img_sampler(event):
    xx = await edit_or_reply(event, "`Sedang Mencari Gambar Yang Anda Cari...`")
    query = event.pattern_match.group(1)
    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 15
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await xx.delete()


@cilik_cmd(pattern="google ([\s\S]*)")
async def gsearch(q_event):
    man = await edit_or_reply(q_event, "`Processing...`")
    match = q_event.pattern_match.group(1)
    page = re.findall(r"-p\d+", match)
    lim = re.findall(r"-l\d+", match)
    try:
        page = page[0]
        page = page.replace("-p", "")
        match = match.replace("-p" + page, "")
    except IndexError:
        page = 1
    try:
        lim = lim[0]
        lim = lim.replace("-l", "")
        match = match.replace("-l" + lim, "")
        lim = int(lim)
        if lim <= 0:
            lim = int(5)
    except IndexError:
        lim = 5
    smatch = match.replace(" ", "+")
    search_args = (str(smatch), int(page))
    gsearch = GoogleSearch()
    bsearch = BingSearch()
    ysearch = YahooSearch()
    try:
        gresults = await gsearch.async_search(*search_args)
    except NoResultsOrTrafficError:
        try:
            gresults = await bsearch.async_search(*search_args)
        except NoResultsOrTrafficError:
            try:
                gresults = await ysearch.async_search(*search_args)
            except Exception as e:
                return await edit_delete(man, f"**ERROR:**\n`{e}`", time=10)
    msg = ""
    for i in range(lim):
        if i > len(gresults["links"]):
            break
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉 [{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await edit_or_reply(
        man,
        "**Keyword Google Search:**\n`" + match + "`\n\n**Results:**\n" + msg,
        link_preview=False,
        aslink=True,
        linktext=f"**Hasil Pencarian untuk Keyword** `{match}` **adalah** :",
    )


@cilik_cmd(pattern="tts(?: |$)([\s\S]*)")
async def text_to_speech(query):
    textx = await query.get_reply_message()
    message = query.pattern_match.group(1)
    xx = await query.reply("Processing...")
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await edit_delete(
            xx, "**Berikan teks atau balas pesan untuk Text-to-Speech!**"
        )
    try:
        gTTS(message, lang=TTS_LANG)
    except AssertionError:
        return await edit_delete(
            xx,
            "**Teksnya kosong.**\n"
            "Tidak ada yang tersisa untuk dibicarakan setelah pra-pemrosesan, pembuatan token, dan pembersihan.",
        )
    except ValueError:
        return await edit_delete(xx, "**Bahasa tidak didukung.**")
    except RuntimeError:
        return await edit_delete(xx, "**Error saat memuat kamus bahasa.**")
    tts = gTTS(message, lang=TTS_LANG)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as audio:
        linelist = list(audio)
        linecount = len(linelist)
    if linecount == 1:
        tts = gTTS(message, lang=TTS_LANG)
        tts.save("k.mp3")
    with open("k.mp3", "r"):
        await query.client.send_file(query.chat_id, "k.mp3", voice_note=True)
        os.remove("k.mp3")
        await xx.delete()


@cilik_cmd(pattern="tr(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    xx = await event.reply("Processing...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "id"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        return await edit_delete(xx, "**.tr <kode bahasa>** sambil reply ke pesan")
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        output_str = """**DITERJEMAHKAN** dari `{}` ke `{}`
`{}`""".format(
            translated.src, lan, after_tr_text
        )
        await xx.edit(output_str)
    except Exception as exc:
        await edit_delete(xx, str(exc))


@cilik_cmd(pattern=r"lang (tr|tts) (.*)")
async def lang(value):
    util = value.pattern_match.group(1).lower()
    xx = await edit_or_reply(value, "`Processing...`")
    if util == "tr":
        scraper = "Translator"
        global TRT_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in LANGUAGES:
            TRT_LANG = arg
            LANG = LANGUAGES[arg]
        else:
            await edit_delete(
                xx,
                f"**Kode Bahasa tidak valid !!**\n**Kode bahasa yang tersedia**:\n\n`{LANGUAGES}`",
            )
            return
    elif util == "tts":
        scraper = "Text to Speech"
        global TTS_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in tts_langs():
            TTS_LANG = arg
            LANG = tts_langs()[arg]
        else:
            await edit_delete(
                xx,
                f"**Kode Bahasa tidak valid!!**\n**Kode bahasa yang tersedia**:\n\n`{tts_langs()}`",
            )
            return
    await xx.edit(f"**Bahasa untuk** `{scraper}` **diganti menjadi** `{LANG.title()}`")


@cilik_cmd(pattern="yt (\d*) *(.*)")
async def yt_search(video_q):
    if video_q.pattern_match.group(1) != "":
        counter = int(video_q.pattern_match.group(1))
        if counter > 10:
            counter = int(10)
        if counter <= 0:
            counter = int(1)
    else:
        counter = int(5)
    query = video_q.pattern_match.group(2)
    if not query:
        await edit_delete(video_q, "`Masukkan keyword untuk dicari`")
    xx = await video_q.reply("Processing...")
    try:
        results = json.loads(YoutubeSearch(query, max_results=counter).to_json())
    except KeyError:
        return await edit_delete(
            xx, "`Pencarian Youtube menjadi lambat.\nTidak dapat mencari keyword ini!`"
        )
    output = f"**Pencarian Keyword:**\n`{query}`\n\n**Hasil:**\n\n"
    for i in results["videos"]:
        try:
            title = i["title"]
            link = "https://youtube.com" + i["url_suffix"]
            channel = i["channel"]
            duration = i["duration"]
            views = i["views"]
            output += f"🏷 **Judul:** [{title}]({link})\n⏱ **Durasi:** {duration}\n👀 {views}\n🖥 **Channel:** `{channel}`\n━━\n"
        except IndexError:
            break

    await xx.edit(output, link_preview=False)


@cilik_cmd(pattern="yt(audio|video( \d{0,4})?) (.*)")
async def download_video(v_url):
    dl_type = v_url.pattern_match.group(1).lower()
    reso = v_url.pattern_match.group(2)
    reso = reso.strip() if reso else None
    url = v_url.pattern_match.group(3)
    xx = await v_url.reply("Preparing to download...")
    s_time = time.time()
    video = False
    audio = False

    if "tiktok.com" in url:
        async with ClientSession() as ses, ses.head(
            url, allow_redirects=True, timeout=5
        ) as head:
            url = str(head.url)

    if "audio" in dl_type:
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "noprogress": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": os.path.join(
                TEMP_DOWNLOAD_DIRECTORY, str(s_time), "%(title)s.%(ext)s"
            ),
            "quiet": True,
            "logtostderr": False,
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "proxy": "",
            "extractor-args": "youtube:player_client=_music",
        }
        audio = True

    elif "video" in dl_type:
        quality = (
            f"bestvideo[height<={reso}]+bestaudio/best[height<={reso}]"
            if reso
            else "bestvideo+bestaudio/best"
        )
        opts = {
            "format": quality,
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "noprogress": True,
            "outtmpl": os.path.join(
                TEMP_DOWNLOAD_DIRECTORY, str(s_time), "%(title)s.%(ext)s"
            ),
            "logtostderr": False,
            "quiet": True,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
            "proxy": "",
            "extractor-args": "youtube:player_client=all",
        }
        video = True

    try:
        await xx.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await edit_delete(xx, f"`{DE}`")
    except ContentTooShortError:
        return await edit_delete(xx, "`The download content was too short.`")
    except GeoRestrictedError:
        return await edit_delete(
            xx,
            "`Video is not available from your geographic location "
            "due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await edit_delete(xx, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await edit_delete(xx, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await edit_delete(
            xx, "`Media is not available in the requested format.`"
        )
    except XAttrMetadataError as XAME:
        return await edit_delete(xx, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await edit_delete(xx, "`There was an error during info extraction.`")
    except Exception as e:
        return await edit_delete(xx, f"{str(type(e))}: {str(e)}")
    c_time = time.time()
    if audio:
        await xx.edit(
            f"**Sedang Mengupload Lagu:**\n`{rip_data.get('title')}`"
            f"\nby **{rip_data.get('uploader')}**"
        )
        f_name = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*.mp3"))[0]
        with open(f_name, "rb") as f:
            result = await upload_file(
                client=v_url.client,
                file=f,
                name=f_name,
                progress_callback=lambda d, t: get_event_loop().create_task(
                    progress(
                        d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp3"
                    )
                ),
            )

        thumb_image = [
            x
            for x in glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))
            if not x.endswith(".mp3")
        ][0]
        metadata = extractMetadata(createParser(f_name))
        duration = 0
        if metadata and metadata.has("duration"):
            duration = metadata.get("duration").seconds
        await v_url.client.send_file(
            v_url.chat_id,
            result,
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=duration,
                    title=rip_data.get("title"),
                    performer=rip_data.get("uploader"),
                )
            ],
            thumb=thumb_image,
        )
        await xx.delete()
    elif video:
        await xx.edit(
            f"**Sedang Mengupload Video:**\n`{rip_data.get('title')}`"
            f"\nby **{rip_data.get('uploader')}**"
        )
        f_path = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))[0]
        # Noob way to convert from .mkv to .mp4
        if f_path.endswith(".mkv") or f_path.endswith(".webm"):
            base = os.path.splitext(f_path)[0]
            os.rename(f_path, base + ".mp4")
            f_path = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))[0]
        f_name = os.path.basename(f_path)
        with open(f_path, "rb") as f:
            result = await upload_file(
                client=v_url.client,
                file=f,
                name=f_name,
                progress_callback=lambda d, t: get_event_loop().create_task(
                    progress(d, t, v_url, c_time, "Uploading..", f_name)
                ),
            )
        thumb_image = await get_video_thumb(f_path, "thumb.png")
        metadata = extractMetadata(createParser(f_path))
        duration = 0
        width = 0
        height = 0
        if metadata:
            if metadata.has("duration"):
                duration = metadata.get("duration").seconds
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
        await v_url.client.send_file(
            v_url.chat_id,
            result,
            thumb=thumb_image,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    supports_streaming=True,
                )
            ],
            caption=f"[{rip_data.get('title')}]({url})",
        )
        os.remove(thumb_image)
        await xx.delete()


@cilik_cmd(pattern="rbg(?: |$)(.*)")
async def kbg(remob):
    if REM_BG_API_KEY is None:
        await edit_delete(
            remob,
            "`Error: Remove.BG API key missing! Add it to environment vars or config.env.`",
        )
        return
    input_str = remob.pattern_match.group(1)
    message_id = remob.message.id
    if remob.reply_to_msg_id:
        message_id = remob.reply_to_msg_id
        reply_message = await remob.get_reply_message()
        xx = await edit_or_reply(remob, "`Processing...`")
        try:
            if isinstance(
                reply_message.media, MessageMediaPhoto
            ) or "image" in reply_message.media.document.mime_type.split("/"):
                downloaded_file_name = await remob.client.download_media(
                    reply_message, TEMP_DOWNLOAD_DIRECTORY
                )
                await xx.edit("`Removing background from this image..`")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await edit_delete(xx, "`Bagaimana cara menghapus latar belakang ini ?`")
        except Exception as e:
            await edit_delete(xx, str(e))
            return
    elif input_str:
        await edit_delete(
            xx, f"`Removing background from online image hosted at`\n{input_str}"
        )
        output_file_name = await ReTrieveURL(input_str)
    else:
        await edit_delete(xx, "`Saya butuh sesuatu untuk menghapus latar belakang.`")
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "removed_bg.png"
            await remob.client.send_file(
                remob.chat_id,
                remove_bg_image,
                force_document=True,
                reply_to=message_id,
            )
            await xx.delete()
    else:
        await edit_delete(
            xx,
            "**Error (Invalid API key, I guess ?)**\n`{}`".format(
                output_file_name.content.decode("UTF-8")
            ),
        )


# this method will call the API, and return in the appropriate format
# with the name provided.
async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )


async def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True,
    )


@cilik_cmd(pattern="web (.*)")
async def capture(url):
    xx = await url.reply("Processing...")
    chrome_options = await options()
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.arguments.remove("--window-size=1920x1080")
    driver = await chrome(chrome_options=chrome_options)
    input_str = url.pattern_match.group(1)
    link_match = match(r"\bhttps?://.*\.\S+", input_str)
    if link_match:
        link = link_match.group()
    else:
        return await edit_delete(xx, "`I need a valid link to take screenshots from.`")
    driver.get(link)
    height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
        "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )
    width = driver.execute_script(
        "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
        "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
        "document.documentElement.offsetWidth);"
    )
    driver.set_window_size(width + 125, height + 125)
    wait_for = height / 1000
    await xx.edit(
        "`Generating screenshot of the page...`"
        f"\n`Height of page = {height}px`"
        f"\n`Width of page = {width}px`"
        f"\n`Waiting ({int(wait_for)}s) for the page to load.`"
    )
    await sleep(int(wait_for))
    im_png = driver.get_screenshot_as_png()
    # saves screenshot of entire page
    driver.quit()
    message_id = url.message.id
    if url.reply_to_msg_id:
        message_id = url.reply_to_msg_id
    with io.BytesIO(im_png) as out_file:
        out_file.name = "screencapture.png"
        await xx.edit("Uploading screenshot as file..")
        await url.client.send_file(
            url.chat_id,
            out_file,
            caption=input_str,
            force_document=True,
            reply_to=message_id,
        )
        await xx.delete()


CMD_HELP.update(
    {
        "Translator": f"**➢ Plugin : **`Translator`\
        \n\n **ᴄᴍᴅ :** `{cmd}tr` <text/reply>\
        \n └⋟ Menerjemahkan teks ke bahasa yang disetel \
        \n\n └⋟ Gunakan {cmd}lang tr <kode bahasa> untuk menyetel bahasa untuk tr **(Bahasa Default adalah bahasa Indonesia)\
    "
    }
)


CMD_HELP.update(
    {
        "Tts": f"**➢ Plugin : **`TextToSpech`\
        \n\n **ᴄᴍᴅ :** `{cmd}tts` <text/reply>\
        \n └⋟ Menerjemahkan teks ke ucapan untuk bahasa yang disetel. \
        \n\n └⋟ Gunakan {cmd}lang tts <kode bahasa> untuk menyetel bahasa untuk tr **(Bahasa Default adalah bahasa Indonesia)**\
    "
    }
)

CMD_HELP.update(
    {
        "RemoveBg": "**➢ Plugin : **`RemoveBg`\
        \n\n **ᴄᴍᴅ :** `{cmd}rbg` <Tautan ke Gambar> atau balas gambar apa pun (Peringatan: tidak berfungsi pada stiker.)\
        \n └⋟ Menghapus latar belakang gambar, menggunakan API remove.bg\
    "
    }
)


CMD_HELP.update(
    {
        "Google": f"**➢ Plugin : **`Google`\
        \n\n **ᴄᴍᴅ :** `{cmd}google` <flags> <query>\
        \n └⋟ Untuk Melakukan pencarian di google (default 5 hasil pencarian)\
        \n └⋟ **Flags :** `-l` **= Untuk jumlah hasil pencarian.**\
        \n └⋟ **Example :** `{cmd}google -l4 yanto` atau `{cmd}google yanto`\
        \n\n **ᴄᴍᴅ :** `{cmd}img` <search_query>\
        \n └⋟ Melakukan pencarian gambar di Google dan menampilkan 15 gambar.\
    "
    }
)


CMD_HELP.update(
    {
        "Youtube": f"**➢ Plugin : **`Youtube`\
        \n\n **ᴄᴍᴅ :** `{cmd}yt` <jumlah> <query>\
        \n └⋟ Melakukan Pencarian YouTube. Dapat menentukan jumlah hasil yang dibutuhkan (default adalah 5)\
        \n\n **ᴄᴍᴅ :** `{cmd}ytaudio` <url>\
        \n └⋟ Untuk Mendownload lagu dari YouTube dengan link.\
        \n\n **ᴄᴍᴅ :** `{cmd}ytvideo` <quality> <url>\
        \n └⋟ Quality : `144`, `240`, `360`, `480`, `720`, `1080`, `2160`\
        \n └⋟ Untuk Mendownload video dari YouTube dengan link.\
        \n\n **ᴄᴍᴅ :** `{cmd}song` <nama lagu>\
        \n └⋟ Untuk mendownload lagu dari youtube dengan nama lagu.\
        \n\n **ᴄᴍᴅ :** `{cmd}vsong` <nama lagu>\
        \n └⋟ Untuk mendownload Video dari youtube dengan nama video.\
    "
    }
)


CMD_HELP.update(
    {
        "Webs": f"**➢ Plugin : **`Webs`\
        \n\n **ᴄᴍᴅ :** `{cmd}web` <url>\
        \n └⋟ Mengambil tangkapan layar dari situs web dan mengirimkan tangkapan layar.\
        \n └⋟ {cmd}web http://www.google.com\
    "
    }
)


