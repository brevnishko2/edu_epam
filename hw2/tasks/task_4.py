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
from typing import Callable, List


def cache(func: Callable) -> Callable:
    """
    :param func: any function for cache
    :return: cached function's return
    """
    cached_value_list: List[list] = []

    def some_func(*args, **kwargs):
        """
        :param args: any args for decorated func
        :param cached_value_dict: dict for cached value
        :return: cached func(*args) result
        """
        for item in cached_value_list:
            if [args, kwargs] in item:
                # if func had already called with this args return cache
                return item[-1]
        else:
            # add value to cache if it isn't in it
            cached_value_list.append([[args, kwargs]])
            cached_value_list[-1].append(func(*args, *kwargs))
            return cached_value_list[-1][-1]

    return some_func
