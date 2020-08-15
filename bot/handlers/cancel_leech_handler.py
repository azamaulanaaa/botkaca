# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /cancel handler

from pyrogram import Client, Message
from bot import LOCAL, CONFIG, STATUS

async def func(client : Client, message: Message):
    if len(message.command()) <= 1:        
        try:
            await message.delete()
        except:
            pass
        
    gid = message.command()[1]
    if STATUS.ARIA2_API:
        aria2_api = STATUS.ARIA2_API
        try:
            download = aria2_api.get_download(gid)
            LOGGER.debug(f'Cancel upload : {download.name}')
            await message.reply_text(
                LOCAL.ARIA2_DOWNLOAD_CANCELED.format(
                    name = download.name
                )
            )
        except Exception as e:
            LOGGER.warn(str(e))
            await message.reply_text(str(e))
    else:
        try:
            await message.delete()
        except:
            pass