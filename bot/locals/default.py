
from bot.locals import Local

LOCAL = Local({
    'NO_HELP_INFO' : 'no information',
    'WRONG_ROOM' : 'I a\'m not suppose to be here.\nID : <code>{CHAT_ID}</code>',
    'WELCOME_MESSAGE' : "Hi!\nI'm <b>Bot</b>!\nPowered by pyrogram.\n\nUse <code>/{cmd_pass} </code>to enter the password.",
    'ARIA2_CHECKING_LINK' : "checking...",
    'ARIA2_DOWNLOAD_STATUS' : "Downloading : <code>{name}</code>\n{block}\nSize : {total_size}\nDN : {download_speed} / UP : {upload_speed}\nETA : {eta}\nID : <code>{gid}</code>",
    'ARIA2_DOWNLOAD_SUCCESS' : 'File downloaded : <code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'Download canceled : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : 'Download auto canceled : <code>{name}</code>\nYour Torrent/Link is Dead.',
    'UPLOADING_FILE' : 'Uploading : <code>{name}</code>',
    'UPLOADING_PROGRESS' : 'Uploading : <code>{name}</code>\n{block}\nSize : {size}\nUP : {upload_speed}/s\nETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : 'Upload : Failed. file not found.\n<code>{name}</code>',
    'SPLIT_FILE' : 'Spliting : <code>{name}</code>',
    'COMMAND_START' : 'start bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'this message',
    'COMMAND_LEECH' : 'leech link or magnet',
    'COMMAND_CANCEL_LEECH' : 'cancel leeching',
    'BLOCK_EMPTY' : "▱",
    "BLOCK_FILLED" : "▰"
})