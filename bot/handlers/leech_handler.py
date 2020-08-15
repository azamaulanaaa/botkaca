from re import match as re_match
from asyncio import sleep as asyncio_sleep
from pyrogram import Client, Message
from aria2p.downloads import Download
from bot import COMMAND, LOCAL, STATUS
from bot.plugins import aria2


async def func(client : Client, message: Message):
    reply = await message.reply_text(LOCAL.ARIA2_CHECKING_LINK)
    aria2_api = STATUS.ARIA2_API or aria2.aria2()
    await aria2_api.start()
    link = message.command[1]
    if isMagnet(link):
        download = aria2_api.add_magnet(link)
        await progress_dl(reply, download)
    else:
        pass

def isMagnet(text):
    return re_match(r'$magnet\:\?xt=urn\:',text)

async def progress_dl(message : Message, download : Download):
    try:
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
                await message.edit_text(text)
            else:
                await message.edit_text(download.error_message)
            await asyncio_sleep(1)
            progress_dl(message, download)
        else:
            await message.edit_text(
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
            await message.edit("<u>error</u> :\n<code>{}</code>".format(str(e)))
            return False