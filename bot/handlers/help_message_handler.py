from pyrogram import Client, Message, Filters
from bot import COMMAND, LOCAL

@Client.on_message(Filters.command(COMMAND.HELP))
async def func(client : Client, message: Message):
    text = LOCAL.HELP_MESSAGE_HEADER + "\n"
    for cmd_code, cmd in COMMAND:
        info = LOCAL.NO_HELP_INFO
        cmd_local = f'COMMAND_{cmd_code}' 
        if cmd_local in dict(LOCAL):
            info = getattr(LOCAL, cmd_local)
        text += f'/{cmd} - {info}\n'
    await message.reply_text(text)