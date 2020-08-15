
# GOAL :
# create status class to hold all status information

import os

class Status:
    __list = {}

    def __init__(self, custom_config = {}):
        self.__list.update(custom_config)

    def __getattr__(self, name):
        if name in self.__list:
            return self.__list[name]
        raise AttributeError

    def __setattr__(self, name, value):
        self.__list[name] = value
    
    def __iter__(self):
        for key in self.__list:
            yield (key, self.__list[key])