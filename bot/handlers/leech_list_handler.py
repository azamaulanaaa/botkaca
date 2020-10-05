# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /list handler

from os.path import join as os_path_join
from pyrogram import Client, Message, Filters
from aria2p import Download
from bot import LOCAL, STATUS, CONFIG, COMMAND
from bot.plugins import aria2

@Client.on_message(Filters.command(COMMAND.LEECH_LIST))
async def func(client: Client, message: Message):
    dir = os_path_join(CONFIG.ROOT, CONFIG.ARIA2_DIR)
    STATUS.ARIA2_API = STATUS.ARIA2_API or aria2.aria2(
        config={
            'dir' : dir
        }
    )
    aria2_api = STATUS.ARIA2_API
    await aria2_api.start()

    downloads = aria2_api.get_downloads()
    text = LOCAL.LEECH_LIST_MESSAGE_HEADER + '\n'
    for download in downloads:
        text += LOCAL.LEECH_LIST_FORMAT.format(
            name = download.name,
            status = download.status,
            gid = download.gid
        )
    await message.reply(text, quote=False)
    if message.chat.type == "private":
        try:
            await message.delete()
        except:
            pass