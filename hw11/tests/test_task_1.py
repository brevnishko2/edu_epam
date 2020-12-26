from hw11.tasks.task_1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_color():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLACK == "BLACK"


def test_sizes():
    assert SizesEnum.XL == "XL"
    assert SizesEnum.M == "M"


def test_iteration():

    actual_result = []
    for i in ColorsEnum():
        actual_result.append(i)

    assert actual_result == ["RED", "BLUE", "ORANGE", "BLACK"]


def test_len():
    assert len(ColorsEnum()) == 4
