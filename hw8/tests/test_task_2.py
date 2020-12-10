import os
from hw8.tasks.task_2 import TableData


path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.sqlite")
presidents = TableData(path, "presidents")


def test_db_iterable():
    count = 0
    for _ in presidents:
        count += 1

    assert count == 3


def test_len_works():
    assert len(presidents) == 3


def test_get_item():
    yeltsin = presidents["Yeltsin"]

    assert yeltsin == ("Yeltsin", 999, "Russia")


def test_contains():
    assert "Yeltsin" in presidents
