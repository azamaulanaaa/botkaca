# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create leech handler class

from re import match as re_match
from asyncio import sleep as asyncio_sleep
from os.path import join as os_path_join
from pyrogram import Client, Message
from aria2p.downloads import Download, File
from bot import COMMAND, LOCAL, STATUS, CONFIG
from bot.plugins import aria2
from bot.handlers import upload_to_tg_handler


async def func(client : Client, message: Message):
    reply = await message.reply_text(LOCAL.ARIA2_CHECKING_LINK)
    dir = os_path_join(CONFIG.ROOT, CONFIG.ARIA2_DIR)
    aria2_api = STATUS.ARIA2_API or aria2.aria2(
        config={
            'dir' : dir
        }
    )
    await aria2_api.start()
    link = " ".join(message.command[1:])
    download = aria2_api.add_magnet(link)
    await progress_dl(reply, aria2_api, download.gid)
    if not download.followed_by_ids:
        for file in downlaod.files:
            await upload_to_tg_handler.func(file.path, reply)
    else:
        for gid in download.followed_by_ids:
            reply = message.reply(f"New download <code>{gid}</code>", quote=False)
            await progress_dl(reply, aria2_api, gid)
            for file in downlaod.files:
                await upload_to_tg_handler.func(file.path, reply)
       

async def progress_dl(message : Message, aria2_api : aria2.aria2, gid : int, previous_text=None):
    try:
        download = aria2_api.get_download(gid)
        if not download.is_complete:
            if not download.error_message:
                text = LOCAL.ARIA2_DOWNLOAD_STATUS.format(
                    name = download.name,
                    download_speed = download.download_speed_string(),
                    upload_speed = download.upload_speed_string(),
                    progress_string = download.progress_string(),
                    eta = download.eta_string(),
                    gid = download.gid
                )
                if text != previous_text:
                    await message.edit(text)
            else:
                await message.edit(download.error_message)
            await asyncio_sleep(1)
            await progress_dl(message, aria2_api, gid, text)
        else:
            await message.edit(
                LOCAL.ARIA2_DOWNLOAD_SUCCESS.format(
                    name=download.name
                )
            )
    except Exception as e:
        if " not found" in str(e) or "'file'" in str(e):
            await message.edit(
                LOCAL.ARIA2_DOWNLOAD_CANCELED.format(
                    name = download.name
                )
            )
            return False
        elif " depth exceeded" in str(e):
            download.remove(force=True)
            await message.edit(
                LOCAL.ARIA2_DEAD_LINK.format(
                    name = download.name
                )
            )
            return False
        else:
            LOGGER.exception(str(e))
            await message.edit("<u>error</u> :\n<code>{}</code>".format(str(e)))
            return False