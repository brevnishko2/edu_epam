from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Первая строчка файла записывается в first_value для
    присвоения первоначального значения
    max_int & min_int. Цикл пробегается по всем строчкам
    сравнивая текущие экстремумы с новыми
    значениями"""
    with open(file_name) as fi:
        first_value = fi.readline()
        max_int, min_int = int(first_value[0]), int(first_value[0])
        for line in fi:
            lst = line.strip().split(",")
            int_lst = list(map(int, lst))
            for i in int_lst:
                max_int = max(max_int, i)
                min_int = min(min_int, i)
        min_max: Tuple[int, int] = (
            min_int,
            max_int,
        )
        return min_max
