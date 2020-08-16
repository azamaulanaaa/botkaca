
# GOAL :
# create config class to hold all config information
# able to load custom config from env vars

import os

class Config:
    __list = {}

    def __init__(self, custom = {}):
        for key in custom:
            if custom[key] == -1:
                custom[key] = self.__evar(key, should_prompt=True)
            else:
                custom[key] = self.__evar(key, custom[key])
        self.__list.update(custom)

    def __getattr__(self, name):
        if name in self.__list:
            return self.__list[name]
        raise AttributeError

    def __evar(self, name: str, default=None, should_prompt=False):
        value = os.environ.get(name, default)
        if not value and should_prompt:
            try:
                value = input(f"enter {name}'s value: ")
            except EOFError:
                value = default
            print("\n")
        return value
    
    def __iter__(self):
        for key in self.__list:
            yield (key, self.__list[key])