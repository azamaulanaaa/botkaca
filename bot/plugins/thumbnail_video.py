# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create video thumbnail maker handler class

from os import path as os_path
import asyncio
import ffmpeg

async def func(filepath):
    if not os_path.exists(filepath):
        return False

    probe = ffmpeg.probe(filepath)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    duration = int(float(video_stream["duration"])/2) or 0

    out_file = filepath + ".jpg"
    
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        filepath,
        '-ss',
        str(duration),
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