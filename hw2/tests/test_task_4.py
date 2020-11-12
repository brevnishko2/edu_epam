import pytest
from time import sleep, time
from hw2.tasks.task_4 import cache


def summa(*a, b=3):
    sleep(1)
    return sum(a, b)


def str_summa(a, b):
    sleep(1)
    return a + b


def some_obj():
    sleep(1)
    return some_obj


def test_summa():
    value = [2, 3, 4]
    start_time = time()
    cache_func = cache(summa)
    actual_result1 = cache_func(*value, b=2)
    actual_result2 = cache_func(*value, b=2)

    assert actual_result1 is actual_result2 and (time() - start_time) < 2


def test_str_summa():
    value = ["qwe", "zxc"]
    start_time = time()
    cache_func = cache(str_summa)
    actual_result1 = cache_func(*value)
    actual_result2 = cache_func(*value)

    assert actual_result1 is actual_result2 and (time() - start_time) < 2


def test_some_obj():
    start_time = time()
    cache_func = cache(some_obj)
    actual_result1 = cache_func()
    actual_result2 = cache_func()

    assert actual_result1 is actual_result2 and (time() - start_time) < 2
