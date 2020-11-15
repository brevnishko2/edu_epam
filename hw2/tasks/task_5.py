"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
"""


def custom_range(iterable, *args, step=1) -> list:
    """
    :param iterable: must be some iterable obj
    :param args: items from iterable
    :return: list[start : end : step] from iterable

    """
    try:
        iter(iterable)
    except TypeError:
        print("first arg must be iterable")
    if len(args) == 1:
        end = args[0]
        start = iterable[0]
    elif len(args) == 2:
        start, end = args
    elif len(args) == 3:
        start, end, step = args
    try:
        result_list = [
            i for i in iterable[iterable.index(start) : iterable.index(end) : step]
        ]
    except ValueError:
        print(
            "something wrong with start/end/step args. "
            + "start/end must be in iterable obj, step must be int"
        )
    return result_list
