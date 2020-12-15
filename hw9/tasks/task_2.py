"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


@contextmanager
def suppressor_generator(error):
    """Suppress error inside
    Args:
        error: error's type

    """
    try:
        yield
    except error:
        pass


class suppressor_class:
    """Suppress error inside
    Args:
        error: error's type

    """

    def __init__(self, error):
        self.error = error

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.error:
            return True
