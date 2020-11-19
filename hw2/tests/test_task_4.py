from time import sleep, time

import pytest
from hw2.tasks.task_4 import cache


def summa(*args):
    sleep(0.5)
    return sum(args)


def str_summa(a, b):
    sleep(0.5)
    return a + b


def some_obj():
    sleep(0.5)
    return some_obj


def test_summa():
    value1 = 1
    value2 = 2
    start_time = time()
    cache_func = cache(summa)
    actual_result1 = cache_func(value1, value2)
    actual_result2 = cache_func(value1, value2)

    assert actual_result1 is actual_result2 and (time() - start_time) < 1


def test_str_summa():
    value = ["qwe", "zxc"]
    start_time = time()
    cache_func = cache(str_summa)
    actual_result1 = cache_func(*value)
    actual_result2 = cache_func(*value)

    assert actual_result1 is actual_result2 and (time() - start_time) < 1


def test_some_obj():
    start_time = time()
    cache_func = cache(some_obj)
    actual_result1 = cache_func()
    actual_result2 = cache_func()

    assert actual_result1 is actual_result2 and (time() - start_time) < 1
