import pytest
from hw1.tasks.task_2 import check_fib


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],
            True,
        ),
        ([13, 21, 34, 55, 89, 144], False),
        ([1, 1], False),
    ],
)
def test_fib(value: int, expected_result: bool):
    actual_result = check_fib(value)

    assert actual_result == expected_result
