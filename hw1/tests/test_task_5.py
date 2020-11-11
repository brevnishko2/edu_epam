import pytest
from hw1.tasks.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([[1, 3, -1, -3, 5, 3, 6, 7], 3], 16),
        ([[5, 0, -3, 2, -5, 1], 3], 2),
        ([[1, -3, -3, -5, 1, -3, 1, 1, 5], 4], 4),
    ],
)
def test_max_subarray_sum(value: list, expected_result: int):
    actual_result = find_maximal_subarray_sum(value[0], value[1])

    assert actual_result == expected_result
