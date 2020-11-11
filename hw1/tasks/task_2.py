from collections.abc import Sequence


def check_fib(data: Sequence[int]) -> bool:
    if len(data) < 3:
        if data[0] == 0 and data[1] == 1:
            return True
        return False
    else:
        if (data[0] == 0 or data[0] == 1) and data[1] == 1:
            for i in range(2, len(data)):
                if data[i] != data[i - 1] + data[i - 2]:
                    return False
            return True
        else:
            return False
