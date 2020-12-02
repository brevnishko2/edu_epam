from hw4.tasks.task_1 import read_magic_number
import os
import tempfile


def test_true_number():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
        fp.write("    2")
    result = read_magic_number(fp.name)
    os.remove(fp.name)

    assert result


def test_false_number():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
        fp.write(" 23 ")
    result = read_magic_number(fp.name)
    os.remove(fp.name)

    assert not result


def test_raise_error():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as fp:
        fp.write("21asd")
    try:
        read_magic_number(fp.name)
    except ValueError:
        os.remove(fp.name)
        assert True
    else:
        assert False
