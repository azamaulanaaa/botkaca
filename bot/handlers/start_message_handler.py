from pyrogram import Client, Message
from bot import COMMAND, LOCAL, CONFIG
from bot.handlers import help_message_handler

async def func(client : Client, message: Message):
    try:
        await message.delete()
    except:
        pass
    welcome_message = LOCAL.WELCOME_MESSAGE
    if CONFIG.BOT_PASSWORD:
        welcome_message += LOCAL.PASS_REQUIRED.format(cmd_pass = COMMAND.PASSWORD)
    await message.reply_text(
        welcome_message,
        disable_web_page_preview=True
    )
    if not CONFIG.BOT_PASSWORD:
        await help_message_handler.func(client, message)
