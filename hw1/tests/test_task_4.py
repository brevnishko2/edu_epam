import pytest
from hw1.tasks.task_4 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            [
                [-1, 3, -5, 1, 1, 1],
                [5, 0, -3, 2, -5, 1],
                [2, -1, -2, 1, 3, 0],
                [2, -4, 1, -4, -2, 1],
            ],
            102,
        ),
        (
            [
                [4, -3, 0, 4, 2, 2],
                [-3, -1, 4, 2, -2, 4],
                [4, -2, -3, 4, -3, 3],
                [5, -4, 2, -4, -2, 0],
            ],
            72,
        ),
        ([[1, 2], [-2, -1], [-1, 2], [0, 2]], 2),
    ],
)
def test_check_sum(value: list, expected_result: int):
    actual_result = check_sum_of_four(value[0], value[1], value[2], value[3])

    assert actual_result == expected_result
