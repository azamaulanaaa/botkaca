from os.path import join as os_path_join
from pyrogram import Client, Message, MessageHandler, Filters, CallbackQueryHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER
from bot.handlers import (
    start_message_handler,
    password_handler,
    wrong_room_handler,
    help_message_handler,
    leech_handler,
    cancel_leech_handler,
    leech_list_handler
)

# Initialize bot
app = Client(
    "Bot",
    bot_token=CONFIG.BOT_TOKEN,
    api_id=CONFIG.API_ID,
    api_hash=CONFIG.API_HASH,
    workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
    workers=343
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

# register /help handler
app.add_handler(
    MessageHandler(
        help_message_handler.func,
        filters=Filters.command(COMMAND.HELP)
    )
)

# register /leech handler
app.add_handler(
    MessageHandler(
        leech_handler.func,
        filters=Filters.command(COMMAND.LEECH)
    )
)

# register /cancel handler
app.add_handler(
    MessageHandler(
        cancel_leech_handler.func,
        filters=Filters.command(COMMAND.CANCEL_LEECH)
    )
)

# register /list handler
app.add_handler(
    MessageHandler(
        leech_list_handler.func,
        filters=Filters.command(COMMAND.LEECH_LIST)
    )
)


# cancel button handler
app.add_handler(
    CallbackQueryHandler(
        cancel_leech_handler.func,
        filters=lambda query: query.data.startswith(COMMAND.CANCEL_LEECH)
    )
)

# forward any message to leech handler
@app.on_message(filters=Filters.private)
async def default_message_handler(client : Client, message : Message):
    message.text = "/" + COMMAND.LEECH + " " + message.text
    return await leech_handler.func(client, message)

if __name__ == '__main__':
    app.run()