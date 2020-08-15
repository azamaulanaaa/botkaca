# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# universal function for uploading file to telegram

from os import path as os_path, listdir as os_lisdir, remove as os_remove, rmdir as os_rmdir
from time import time
from math import floor
from pyrogram import Message
from bot import COMMAND, LOCAL, CONFIG
from bot.plugins import formater

async def func(filepath: str, message: Message, delete=False):
    if not os_path.exists(filepath):
        LOGGER.error(f'File not found : {filepath}')
        await message.edit_text(
            LOCAL.UPLOAD_FAILED_FILE_MISSING.format(
                name = os_path.basename(filepath)
            )
        )
        return

    if os_path.isdir(filepath):
        await message.delete()
        ls = os_lisdir(filepath)
        for filepath in ls:
            message = await message.reply_text(
                LOCAL.UPLOADING_FILE.format(
                    name = os_path.basename
                )
            )
            await func(filepath, message, delete)
        if delete:
            os_rmdir(filepath)
        return

    video = ['.mp4','.avi','.mkv']
    photo = ['.jpg','.jpeg','.png']

    file_ext = os_path.splitext(filepath)[1]
    info = {
        "start_time" : time(),
        "name" : os_path.basename(filepath)
    }
    upload_fn = None

    if file_ext in photo:
        upload_fn = message.reply_photo
    elif file_ext in video:
        upload_fn = message.reply_video
    else:
        upload_fn = message.reply_document
    
    LOGGER.debug(f'Uploading : {filepath}')
    await upload_fn(
        filepath,
        progress=progress_upload_tg,
        progress_args=(
            message,
            info
        )
    )
    LOGGER.debug(f'Uploaded : {filepath}')
    await message.delete()
    if delete:
        os_remove(filepath)

async def progress_upload_tg(current, total, message, info):
    percentage = round(current * 100 / total)
    block = ""
    for i in range(10):
        if i <= floor(percentage/10):
            block += "▰"
        else:
            block += "▱"
    time_passed = time() - info["start_time"]
    await message.edit(
        LOCAL.UPLOADING_PROGRESS.format(
            name = info["name"],
            block = block,
            percentage = f"{percentage}%",
            upload_speed = formater.format_bytes(current / time_passed),
            eta = formater.format_time(total * time_passed / current)
        )
    )