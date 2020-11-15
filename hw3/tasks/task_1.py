"""In previous homework task 4, you wrote a cache function that remembers
other function output value.
 Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only.
"""
from typing import Callable


def cache(*arg, **kwarg) -> Callable:
    """
    :param func: any function for cache
    :return: cached function's return
    """

    def cached_func(func):
        cached_value_dict = {}
        cache_counter = kwarg["times"]

        def some_func(*args, **kwargs):
            """
            :param args: any args for decorated func
            :param cached_value_dict: dict for cached value
            :return: cached func(*args) result
            """
            # if func had already called with this args return cached value
            if (tuple(args), tuple(kwargs)) in cached_value_dict:
                # takes counter from outside function
                nonlocal cache_counter
                if cache_counter > 1:
                    cache_counter -= 1
                    return cached_value_dict[(tuple(args), tuple(kwargs))]
                else:
                    # return value last time and delete if from dict
                    return cached_value_dict.pop((tuple(args), tuple(kwargs)))
            else:
                # add value to cache if it isn't in it
                cached_value_dict[(tuple(args), tuple(kwargs))] = func(*args, **kwargs)
                return cached_value_dict[(tuple(args), tuple(kwargs))]

        return some_func

    return cached_func
