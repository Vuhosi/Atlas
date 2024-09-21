from typing import Callable
import inspect

class Tool():
    def __init__(self, func: Callable):
        self.name = func.__name__
        self.func = func
        self.desc = inspect.getdoc(func) or ""

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
