# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# handling file upload using bytesio

from io import FileIO
from os import path as os_path, remove as os_remove

class ChunkIO(FileIO):

    def __init__(self, filepath, pos=0, size=-1):
        FileIO.__init__(self, filepath, 'rb')
        self.name = os_path.basename(filepath)
        self.__filepath__ = filepath
        self.__startpos__ = pos
        self.__size__ = size
        self.__currentpos__ = 0

        total_size = os_path.getsize(filepath) - pos
        if self.__size__ > total_size:
            self.__size__ = total_size

    
    def read(self, size = -1):
        if size == -1 or size + self.__currentpos__ > self.__size__:
            size =  self.__size__ - self.__currentpos__
        self.__currentpos__ += size
        return FileIO.read(self, size)
    
    def seek(self, position, whence=0):
        if whence == 1:
            position += self.__currentpos__
        elif whence == 2:
            position += self.__size__
            
        self.__currentpos__ = position
        FileIO.seek(self, self.__startpos__ + position)
        return position
    
    def tell(self):
        return self.__currentpos__
