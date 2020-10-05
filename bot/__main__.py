from os.path import join as os_path_join
from pyrogram import Client, Message, MessageHandler, Filters, CallbackQueryHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER
from bot.handlers import *

# Initialize bot
app = Client(
    "Bot",
    bot_token=CONFIG.BOT_TOKEN,
    api_id=CONFIG.API_ID,
    api_hash=CONFIG.API_HASH,
    workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
    workers=343,
    plugins=dict(root="bot/handlers")
)
app.set_parse_mode("html")

# register /start handler
app.add_handler(
    MessageHandler(
        start_message_handler.func,
        filters=Filters.command(COMMAND.START)
    )
)

if CONFIG.BOT_PASSWORD:
    # register /pass handler
    app.add_handler(
        MessageHandler(
            password_handler.func,
            filters = Filters.command(COMMAND.PASSWORD)
        )
    )

    # take action on unauthorized chat room
    app.add_handler(
        MessageHandler(
            wrong_room_handler.func,
            filters = lambda msg: not msg.chat.id in CONFIG.CHAT_ID
        )
    )

if __name__ == '__main__':
    app.run()