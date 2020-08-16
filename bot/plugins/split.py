# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create split handler class

from os import path as os_path
import asyncio
from glob import glob

async def func(filepath, size):
    if not os_path.isfile(filepath):
        return False

    cmd = [
        "split",
        "--numeric-suffixes=1",
        "--suffix-length=3",
        f"--bytes={size}",
        filepath,
        filepath + "."
    ]
    LOGGER.debug(cmd)

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await process.communicate()

    list = glob(filepath + ".*")
    LOGGER.debug(list)
    return list