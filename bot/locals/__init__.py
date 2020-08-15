# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create local class to hold all localization 

class Local:
    __list = {}

    def __init__(self, custom = {}):
        self.__list.update(custom)

    def __getattr__(self, name):
        if name in self.__list:
            return self.__list[name]
        raise AttributeError
    
    def __iter__(self):
        for key in self.__list:
            yield (key, self.__list[key])
