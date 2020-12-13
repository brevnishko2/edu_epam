import pytest
from hw9.tasks.task_2 import suppressor_generator, SuppressorClass


def test_index_error_suppressed():
    with suppressor_generator(IndexError):
        _ = [][2]
    with SuppressorClass(IndexError):
        _ = [][2]

    assert True


def test_generator_another_error_raises():
    with pytest.raises(IndexError):
        with suppressor_generator(ValueError):
            _ = [][2]


def test_class_another_error_raises():
    with pytest.raises(IndexError):
        with SuppressorClass(ValueError):
            _ = [][2]
