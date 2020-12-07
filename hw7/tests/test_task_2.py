import pytest
from hw7.tasks.task_2 import backspace_compare


@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ("qsd#bh###v", "##qvv#", True),
        ("###", "b####", True),
        ("###a", "#ab", False),
        ("", "#", True),
    ],
)
def test_backspace(value1: str, value2: str, expected_result: bool):
    actual_result = backspace_compare(value1, value2)

    assert actual_result == expected_result
