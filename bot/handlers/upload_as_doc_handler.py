from pyrogram import Client, Message, Filters
from bot import LOCAL, STATUS, COMMAND

@Client.on_message(Filters.command(COMMAND.UPLOAD_AS_DOC))
async def func(client : Client, message: Message):
    STATUS.UPLOAD_AS_DOC = not STATUS.UPLOAD_AS_DOC
    await message.reply_text(LOCAL.UPLOAD_AS_DOC.format(status=STATUS.UPLOAD_AS_DOC))