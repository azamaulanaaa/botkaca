from os.path import join as os_path_join
from pyrogram import Client, Message, MessageHandler, Filters, CallbackQueryHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER, STATUS
from bot.handlers import *
import asyncio

# Initialize bot
app = Client(
    "Bot",
    bot_token=CONFIG.BOT_TOKEN,
    api_id=CONFIG.API_ID,
    api_hash=CONFIG.API_HASH,
    workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
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
            filters = lambda msg: not msg.chat.id in STATUS.CHAT_ID
        )
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(app.start())
    try:
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        loop.run_until_complete(app.stop())
        loop.close()