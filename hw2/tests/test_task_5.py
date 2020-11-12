import string

import pytest
from hw2.tasks.task_5 import custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(value: list, expected_result: list):
    actual_result = custom_range(*value)

    assert actual_result == expected_result


def test_1():
    assert ["a", "b", "c", "d", "e", "f"] == custom_range(string.ascii_lowercase, "g")


def test_2():
    assert ["g", "h", "i", "j", "k", "l", "m", "n", "o"] == custom_range(
        string.ascii_lowercase, "g", "p"
    )


def test_3():
    assert ["p", "n", "l", "j", "h"] == custom_range(
        string.ascii_lowercase, "p", "g", -2
    )


def test_4():
    assert ["5", "e", "n", "w", "F", "O", "X", "'", ":", "]"] == custom_range(
        string.printable, "5", "~", 9
    )


def test_5():
    objects = [object() for _ in range(5)]
    assert objects[2:3] == custom_range(objects, objects[2], objects[3])
