"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable, ca={}) -> Callable:
    """
    :param func: any function for cache
    :param ca: don't touch this
    :return: cached function's return
    :rtype: function's rtype
    """

    def some_func(*args):
        if func(*args) in ca:
            return ca[func(*args)]
        else:
            ca[func(*args)] = func(*args)
            return ca[func(*args)]

    return some_func
