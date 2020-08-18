# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create ffprobe handler

import asyncio
from os import path as os_path
from json import loads as json_loads

async def func(filepath):
    if not os_path.isfile(filepath):
        return False
    
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        'json',
        "-show_format",
        '-show_streams',
        filepath
    ]
    LOGGER.debug(cmd)

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    LOGGER.debug("[stdout] " + stdout.decode())
    LOGGER.debug("[stderr] " + stderr.decode())
    
    info = json_loads(stdout.decode())
    return info