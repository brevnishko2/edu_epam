import os

from hw1.tasks.task_3 import find_maximum_and_minimum


def test_find_max_min():
    path = os.path.abspath(os.path.dirname(__file__)) + "/text_task_3.txt"
    actual_result = find_maximum_and_minimum(path)

    assert actual_result == (1, 345)
