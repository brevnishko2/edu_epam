from hw3.tasks.task_4 import is_armstrong
import pytest


@pytest.mark.parametrize(
    ["value", "expected_result"], [(370, True), (15, False), (153, True), (10, False)],
)
def test_is_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)

    assert actual_result == expected_result
