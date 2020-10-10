
# GOAL :
# create config class to hold all config information
# able to load custom config from env vars

import os

class Config:
    def __init__(self, custom = {}, prefix = ''):
        self.prefix = prefix
        for key in custom:
            self.__setattr__(key,self.__evar(key, custom[key], bool(custom[key] == None)))

    def __evar(self, name: str, default=None, should_prompt=False):
        name = self.prefix + name
        value = os.environ.get(name, default)
        if not value and should_prompt:
            try:
                value = input(f"enter {name}'s value: ")
            except EOFError:
                value = default
            print("\n")
        return value
    
    def __iter__(self):
        for key in self.__dict__:
            yield (key, self.__dict__[key])