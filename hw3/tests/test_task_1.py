import pytest
from hw3.tasks.task_1 import cache


@cache(times=1)
def summa(*args):
    return sum(args)


@cache(times=3)
def some_obj():
    return some_obj


def test_summa():
    value1 = 300
    value2 = 400
    actual_result1 = summa(value1, value2)
    actual_result2 = summa(value1, value2)
    actual_result3 = summa(value1, value2)
    actual_result4 = summa(value1, value2)

    assert (actual_result3 is actual_result4) and (actual_result1 is not actual_result3)
