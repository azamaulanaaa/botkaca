# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create video thumbnail maker handler class

from os import path as os_path
import asyncio
from bot.plugins import ffprobe

async def func(filepath):
    if not os_path.exists(filepath):
        LOGGER.error('File not found : ' + filepath)
        return False

    probe = await ffprobe.func(filepath)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

    try:
        duration = float(video_stream["duration"]) // 2
    except:
        duration = 0

    out_file = filepath + ".jpg"
    
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        filepath,
        '-ss',
        str(duration),
        '-vframes',
        '1',
        '-vf',
        'scale=320:-1',
        '-y',
        out_file
    ]
    LOGGER.debug(cmd)

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await process.communicate()

    LOGGER.debug('Thumbnail : ' + out_file)
    return out_file