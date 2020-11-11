import pytest
from hw2.tasks.task_4 import cache


def summa(*a):
    return sum(*a)


def str_summa(a, b):
    return a + b


def some_obj():
    return some_obj


def test_summa():
    value = [2, 3, 4]
    cache_func = cache(summa)
    actual_result1 = cache_func(value)
    actual_result2 = cache_func(value)

    assert actual_result1 is actual_result2


def test_str_summa():
    value = ["qwe", "zxc"]
    cache_func = cache(str_summa)
    actual_result1 = cache_func(*value)
    actual_result2 = cache_func(*value)

    assert actual_result1 is actual_result2


def test_some_obj():
    cache_func = cache(some_obj)
    actual_result1 = cache_func()
    actual_result2 = cache_func()

    assert actual_result1 is actual_result2
