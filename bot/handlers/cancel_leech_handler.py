# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /cancel handler

from pyrogram import Client, Message, CallbackQuery
from bot import LOCAL, CONFIG, STATUS
from typing import Union

async def func(client : Client, data : Union[Message, CallbackQuery]):
    gid = ""
    update_fn = None
    if type(data) is Message:
        text = data.text
        gid = " ".join(text.split(" ")[1:])
        if not gid:               
            try:
                await data.delete()
            except:
                pass
            return False
        update_fn = data.reply_text
    elif type(data) is CallbackQuery:
        text = data.data
        gid = " ".join(text.split(" ")[1:])
        if not gid:
            return False
        update_fn = data.message.reply_text
    else:
        return False
    
    if STATUS.ARIA2_API:
        aria2_api = STATUS.ARIA2_API
        try:
            download = aria2_api.get_download(gid)
            download.remove(force=True, files=True)
            LOGGER.debug(f'Cancel upload : {download.name}')
            await update_fn(
                LOCAL.ARIA2_DOWNLOAD_CANCELED.format(
                    name = download.name
                )
            )
        except Exception as e:
            LOGGER.warn(str(e))
            await update_fn(str(e))
    else:
        if type(data) is Message:
            try:
                await data.delete()
            except:
                pass