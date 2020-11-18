from hw4.tasks.task_3 import my_precious_logger
import os
import tempfile
from contextlib import redirect_stderr, redirect_stdout


def test_stderr():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
        path = fp.name
    with open(path, "w") as error_file:
        with redirect_stderr(error_file):
            my_precious_logger("error: not enough gold")
    with open(path, "r") as error_file:
        actual_result = error_file.readline()
    os.remove(path)

    assert actual_result == "error: not enough gold"


def test_stdout():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
        path = fp.name
    with open(path, "w") as out_file:
        with redirect_stdout(out_file):
            my_precious_logger("need to build zuggurat")
    with open(path, "r") as out_file:
        actual_result = out_file.readline()
    os.remove(path)

    assert actual_result == "need to build zuggurat"
