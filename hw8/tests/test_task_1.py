import os
import pytest
from hw8.tasks.task_1 import WrapperForStorage


path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "bad_data.txt")
path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt")


def test_bad_value():
    with pytest.raises(ValueError):
        WrapperForStorage(path1)


def test_wrapper():
    test1 = WrapperForStorage(path2)

    assert test1.song == "shadilay"
    assert test1["song"] == "shadilay"
    assert isinstance(test1.power, int)
    assert test1.__doc__ != "docstring_that_never_be_used"
