import pytest
from hw7.tasks.task_3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["value1", "expected_result"],
    [
        (
            [
                ["o", "o", "x", "x"],
                ["x", "o", "o", "x"],
                ["o", "x", "o", "o"],
                ["x", "-", "x", "o "],
            ],
            "o wins!",
        ),
        ([["o", "o", "x"], ["x", "-", "o"], ["o", "x", "o"]], "unfinished"),
        ([["o", "o", "x"], ["x", "x", "o"], ["o", "x", "o"]], "draw!"),
    ],
)
def test_tic_tac_toe(value1: list[list], expected_result: str):
    actual_result = tic_tac_toe_checker(value1)

    assert actual_result == expected_result
