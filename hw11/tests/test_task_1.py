from hw11.tasks.task_1 import SimplifiedEnum


def test_color():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLACK == "BLACK"


def test_sizes():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert SizesEnum.XL == "XL"
    assert SizesEnum.M == "M"
