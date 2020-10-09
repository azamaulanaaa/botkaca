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
    if os_path.getsize(filepath) <= size:
        with FileIO(filepath, 'rb') as f:
            f.name = os_path.basename(filepath)
            f.path = filepath
            yield f
    else:
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
                    pos += size
                    f.name = os_path.basename(filepath) + f'.{index:03d}'
                    yield f

async def video(filepath, size):
    if not os_path.isfile(filepath):
        LOGGER.error('File not found : ' + filepath)
        raise Exception('File not found')
    
    file_path_name, file_ext = os_path.splitext(filepath)
    probe = await ffprobe.func(filepath)
    
    duration = float(probe['format']["duration"])
    size = size * 98 // 100

    splited_duration = 0
    i = 0
    while splited_duration < duration:    
        i+=1
        out_file = file_path_name + f".{i:03d}" + file_ext
        
        cmd = [
            "ffmpeg",
            "-hide_banner",
            '-ss',
            str(splited_duration),
            "-i",
            filepath,
            '-fs',
            str(size),
            '-c',
            'copy',
            '-async',
            '1',
            '-y',
            out_file
        ]
        LOGGER.debug(cmd)

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        LOGGER.debug(f'[stdout] {stdout.decode()}')
        if not stderr.decode():
            LOGGER.error(f'[stderr] {stderr.decode()}')

        splited_duration += float((await ffprobe.func(out_file))['format']["duration"])
        
        LOGGER.debug(out_file)
        yield out_file