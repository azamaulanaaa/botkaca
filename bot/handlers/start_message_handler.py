from pyrogram import Client, Message
from bot import COMMAND, LOCAL, CONFIG
from bot.handlers import help_message_handler

async def func(client : Client, message: Message):
    try:
        await message.delete()
    except:
        pass
    await message.reply_text(
        LOCAL.WELCOME_MESSAGE.format(cmd_pass = COMMAND.PASSWORD),
        disable_web_page_preview=True
    )
    if not CONFIG.BOT_PASSWORD:
        await help_message_handler.func(client, message)
