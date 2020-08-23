# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create split handler class

from os import path as os_path, remove as os_remove
from io import FileIO
import asyncio
from bot.plugins import ffprobe, IOHandler

async def func(filepath, size):
    file_ext = os_path.splitext(filepath)[1]
    video_units = ['.mp4','.mkv','.avi','.webm','.wmv','.mov']
    if file_ext in video_units:
        async for splitted_video in video(filepath, size):
            with FileIO(splitted_video, 'rb') as f:
                f.name = os_path.basename(splitted_video)
                f.path = splitted_video
                yield f
            os_remove(splitted_video)
    else:
        total_size = os_path.getsize(filepath)
        pos = 0
        index = 0
        while pos < total_size:
            index += 1
            with IOHandler.ChunkIO(filepath, pos, size) as f:
                prefix = ''
                if size < total_size:
                    prefix = f'.{index:03d}'
                pos += size
                f.name = os_path.basename(filepath) + prefix
                yield f

async def video(filepath, size):
    supported = ['.mp4','.mkv','.avi','.webm','.wmv','.mov']
    if not os_path.isfile(filepath):
        LOGGER.error('File not found : ' + filepath)
        raise Exception('File not found')
    
    file_path_name, file_ext = os_path.splitext(filepath)
    if not file_ext in supported:
        LOGGER.error('File not supported : ' + filepath)
        raise Exception('File not supported')

    probe = await ffprobe.func(filepath)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    duration = int(float(video_stream["duration"]))

    splited_duration = 0
    i = 0
    while splited_duration < duration:    
        i+=1
        out_file = file_path_name + ".{:03d}".format(i) + file_ext
        
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-i",
            filepath,
            '-ss',
            str(splited_duration),
            '-fs',
            str(size * 99/100),
            '-c',
            'copy',
            '-async',
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
    
        probe = await ffprobe.func(out_file)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

        splited_duration += int(float(video_stream["duration"]))
        
        LOGGER.debug(out_file)
        yield out_file