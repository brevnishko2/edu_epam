import pytest
from hw2.tasks.task_2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], (2, 3)),
        ([2, 2, 1, 1, 1, 2, 2], (1, 2)),
        ([5, 5, 4, 4, 4, 0, 0, 0, 0, 0], (5, 0)),
    ],
)
def test_major_and_minor_elem(value: list, expected_result: tuple):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
