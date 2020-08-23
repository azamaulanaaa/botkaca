# GOAL:
# load config

import os
from bot.config import Config

CONFIG = Config({
    'ROOT' : os.getcwd(),
    'WORKDIR' : 'sessions',
    'LOG_FILE' : 'log.txt',
    'MAX_LOG_SIZE' : 10 * 1024 * 1024,
    'API_HASH' : -1,
    'API_ID' : -1,
    'BOT_TOKEN' : -1,
    'BOT_PASSWORD' : -1,
    'CHAT_ID' : [],
    'EDIT_SLEEP' : 3,
    'UPLOAD_MAX_SIZE' : 2000 * 1024 * 1024,
    'ARIA2_DIR' : 'downloads'
})

# GOAL:
# prepare workdir

workdir = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR)
if not os.path.isdir(workdir):
    os.mkdir(workdir)
del workdir

# GOAL:
# logging any important sign

logfile = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR, CONFIG.LOG_FILE)

if os.path.exists(logfile):
    with open(logfile, "r+") as f_d:
        f_d.truncate(0)

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            logfile,
            maxBytes=CONFIG.MAX_LOG_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# GOAL:
# Log configuration

LOGGER.info(dict(CONFIG))

del logfile

# GOAL:
# Localization

from bot.locals.default import LOCAL

# GOAL:
# load Command format

from bot.command import Command

COMMAND = Command({
    'START' : 'start',
    'PASSWORD' : 'pass',
    'HELP' : 'help',
    'LEECH' : 'leech',
    'CANCEL_LEECH' : 'cancel',
    'LEECH_LIST' : 'list'
})

# GOAL:
# set status

from time import time
from bot.status import Status

STATUS = Status({
    'START_TIME' : time(),
    'ARIA2_API' : None
})
