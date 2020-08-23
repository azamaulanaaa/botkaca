# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /leech handler

from re import match as re_match
from asyncio import sleep as asyncio_sleep
from os.path import join as os_path_join
from math import floor
from pyrogram import Client, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aria2p.downloads import Download, File
from bot import LOCAL, STATUS, CONFIG, COMMAND
from bot.plugins import aria2
from bot.handlers import upload_to_tg_handler
from bot.handlers import cancel_leech_handler

async def func(client : Client, message: Message):
    args = message.text.split(" ")
    if len(args) <= 1:        
        try:
            await message.delete()
        except:
            pass
        return
        
    reply = await message.reply_text(LOCAL.ARIA2_CHECKING_LINK)
    dir = os_path_join(CONFIG.ROOT, CONFIG.ARIA2_DIR)
    STATUS.ARIA2_API = STATUS.ARIA2_API or aria2.aria2(
        config={
            'dir' : dir
        }
    )
    aria2_api = STATUS.ARIA2_API
    await aria2_api.start()

    link = " ".join(args[1:])
    LOGGER.debug(f'Leeching : {link}')

    try:
        download = aria2_api.add_uris([link], options={'continue_downloads' : True})
    except Exception as e:
        if "No URI" in str(e):
            await reply.edit_text(
                LOCAL.ARIA2_NO_URI
            )
            return
        else:
            LOGGER.error(str(e))
            await reply.edit_text(
                str(e)
            )
            return

    if await progress_dl(reply, aria2_api, download.gid):
        upload_status = True
        download = aria2_api.get_download(download.gid)
        if not download.followed_by_ids:
            download.remove(force=True)
            for file in download.files:
                upload_status = await upload_to_tg_handler.func(
                    os_path_join(dir, file.path),
                    client,
                    reply,
                    delete=True
                )
        else:
            gids = download.followed_by_ids
            download.remove(force=True, files=True)
            for gid in gids:
                if await progress_dl(reply, aria2_api, gid):
                    download = aria2_api.get_download(gid)
                    download.remove(force=True)
                    for file in download.files:
                        upload_status = await upload_to_tg_handler.func(
                            os_path_join(dir, file.path),
                            client,
                            reply,
                            delete=True
                        )
        if not upload_status:
            await reply.delete()
    

async def progress_dl(message : Message, aria2_api : aria2.aria2, gid : int, previous_text=None):
    try:
        download = aria2_api.get_download(gid)
        if not download.is_complete:
            if not download.error_message:
                block = ""
                for i in range(1, 11):
                    if i <= floor(download.progress/10):
                        block += LOCAL.BLOCK_FILLED
                    else:
                        block += LOCAL.BLOCK_EMPTY
                text = LOCAL.ARIA2_DOWNLOAD_STATUS.format(
                    name = download.name,
                    block = block,
                    total_size = download.total_length_string(),
                    download_speed = download.download_speed_string(),
                    upload_speed = download.upload_speed_string(),
                    eta = download.eta_string(),
                    gid = download.gid
                )
                if text != previous_text:
                    await message.edit(
                        text,
                        reply_markup=
                            InlineKeyboardMarkup([[
                                InlineKeyboardButton(
                                    COMMAND.CANCEL_LEECH,
                                    callback_data=COMMAND.CANCEL_LEECH + " " + download.gid,
                                    
                                )
                            ]])
                    )
                await asyncio_sleep(int(CONFIG.EDIT_SLEEP))
                return await progress_dl(message, aria2_api, gid, text)
            else:
                await message.edit(download.error_message)
        else:
            await message.edit(
                LOCAL.ARIA2_DOWNLOAD_SUCCESS.format(
                    name=download.name
                )
            )
            return True
    except Exception as e:
        if " not found" in str(e) or "'file'" in str(e):
            await message.delete()
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