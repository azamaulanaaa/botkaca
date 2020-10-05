# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /set_tracker handler


from pyrogram import Client, Message, Filters
from bot import LOCAL, STATUS, CONFIG, COMMAND

@Client.on_message(Filters.command(COMMAND.SET_TRACKER))
async def set(client : Client, message: Message):
    args = message.text.split(" ")
    if len(args) <= 1:
        STATUS.DEFAULT_TRACKER = []
        LOGGER.info('Default Tracker : rested')
        return await message.reply_text(LOCAL.TRACKER_RESET)

    STATUS.DEFAULT_TRACKER = (" ".join(args[1:])).split('\n')
    LOGGER.info('Default Tracker :\n' + '\n'.join(STATUS.DEFAULT_TRACKER))
    return await message.reply_text(LOCAL.TRACKER_APPLIED)

    