# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create video thumbnail maker handler class

from os import path as os_path
import asyncio

async def func(filepath):
    if not os_path.exists(filepath):
        return False

    out_file = filepath + ".jpg"
    
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        filepath,
        '-vf',
        'thumbnail,scale=320:-1',
        '-frames:v',
        '1',
        out_file
    ]
    LOGGER.debug(cmd)

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await process.communicate()

    return out_file