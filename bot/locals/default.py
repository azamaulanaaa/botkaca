
from bot.locals import Local

LOCAL = Local({
    'HELP_MESSAGE_HEADER' : '<b>Bot Command</b>',
    'NO_HELP_INFO' : 'no information',
    'WRONG_ROOM' : 'I a\'m not suppose to be here.\nID : <code>{CHAT_ID}</code>',
    'WELCOME_MESSAGE' : "Hi!\nI'm <b>Bot</b>!\nPowered by pyrogram.\nFork: <a href='https://github.com/azamaulanaaa/botkaca'>github</a>\n\nUse <code>/{cmd_pass} </code>to enter the password.",
    'LEECH_LIST_MESSAGE_HEADER' : '<b>Leech Status</b>',
    'LEECH_LIST_FORMAT' : 'Name: <code>{name}</code>\nStatus: {status}\nID: <code>{gid}</code>\n\n',
    'ARIA2_CHECKING_LINK' : "checking...",
    'ARIA2_DOWNLOAD_STATUS' : "Downloading : <code>{name}</code>\n{block}\nSize : {total_size}\nDN : {download_speed} / UP : {upload_speed}\nETA : {eta}\nID : <code>{gid}</code>",
    'ARIA2_DOWNLOAD_SUCCESS' : 'File downloaded : <code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'Download canceled : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : 'Download auto canceled : <code>{name}</code>\nYour Torrent/Link is Dead.',
    'ARIA2_NO_URI' : 'Link is invalid.',
    'UPLOADING_FILE' : 'Uploading : <code>{name}</code>',
    'UPLOADING_PROGRESS' : 'Uploading : <code>{name}</code>\n{block}\nSize : {size}\nUP : {upload_speed}/s\nETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : 'Upload : Failed. file not found.\n<code>{name}</code>',
    'GENERATE_THUMBNAIL' : 'Thumbnail : Generating.\n<code>{name}</code>',
    'SPLIT_FILE' : 'Spliting : <code>{name}</code>',
    'SPLIT_FAILED' : 'Split : Failed.\n<code>{name}</code>',
    'COMMAND_START' : 'start bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'this message',
    'COMMAND_LEECH' : 'leech link or magnet',
    'COMMAND_CANCEL_LEECH' : 'cancel leeching',
    'COMMAND_LEECH_LIST' : 'list on going leech',
    'BLOCK_EMPTY' : "▱",
    "BLOCK_FILLED" : "▰"
})