from pyrogram import Client, Message
from bot import LOCAL, STATUS

async def func(client : Client, message: Message):
    STATUS.UPLOAD_AS_DOC = not STATUS.UPLOAD_AS_DOC
    await message.reply_text(LOCAL.UPLOAD_AS_DOC.format(status=STATUS.UPLOAD_AS_DOC))