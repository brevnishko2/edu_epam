import pytest

from hw11.tasks.task_2 import Order


def morning():
    return 0.15


def evening():
    return 0.05


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([100, morning], 85.0), ([100, evening], 95.0), ([100], 100),],
)
def test_different_discount_is_working(value, expected_result):
    actual_result = Order(*value).final_price()

    assert actual_result == expected_result
