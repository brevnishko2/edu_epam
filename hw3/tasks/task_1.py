"""In previous homework task 4, you wrote a cache function that remembers
other function output value.
 Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only.
"""
from typing import Callable


def cache(times=None) -> Callable:
    """
    take 1 function and cache result with count = times
    :arg:
        func: any callable
    :return:
        decorated func: callable
    """

    def cached_func(func):
        cached_value_dict = {}
        if times:
            cache_counter = times

        def some_func(*args, **kwargs):
            # if func had already called with this args return cached value
            if (args, tuple(kwargs.items())) in cached_value_dict:
                # takes counter from outside function
                nonlocal cache_counter
                if cache_counter > 1:
                    cache_counter -= 1
                    return cached_value_dict[(args, tuple(kwargs.items()))]
                else:
                    # return value last time and delete if from dict
                    return cached_value_dict.pop((args, tuple(kwargs.items())))
            else:
                # add value to cache if it isn't in it
                cached_value_dict[(args, tuple(kwargs.items()))] = func(*args, **kwargs)
                return cached_value_dict[(args, tuple(kwargs.items()))]

        return some_func

    return cached_func
