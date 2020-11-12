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


def cache(func: Callable) -> Callable:
    """
    :param func: any function for cache
    :return: cached function's return
    """

    def some_func(*args, cached_value_dict={}, **kwargs):
        """
        :param args: any args for decorated func
        :param cached_value_dict: dict for cached value
        :return: cached func(*args) result
        """
        if (tuple(args), tuple(kwargs)) in cached_value_dict:
            # if func had already called with this args return cached value
            return cached_value_dict[(tuple(args), tuple(kwargs))]
        else:
            # add value to cache if it isn't in it
            cached_value_dict[(tuple(args), tuple(kwargs))] = func(*args, **kwargs)
            return cached_value_dict[(tuple(args), tuple(kwargs))]

    return some_func
