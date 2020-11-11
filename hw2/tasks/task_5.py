"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(iterable, *args):
    """
    :param iterable: must be some iterable obj
    :type iterable: iterable
    :param args: items from iterable
    if there's only 1 arg:
        arg_1 = end
    else:
        arg_1 = start
        arg_2 = end
        arg_3 = step
    :return: 1 arg: iterable[0: arg]
        2 args: iterable[arg_1:arg_2]
        3 args: iterable[arg_1:arg_2:arg_3]
    :rtype: list

    """
    result_list = []
    if len(args) == 1:
        end = args[0]
        for i in iterable:
            if i != end:
                result_list.append(i)
            else:
                return result_list
    elif len(args) == 2:
        start, end = args
        for i in iterable[iterable.index(start) : iterable.index(end)]:
            result_list.append(i)
        return result_list
    elif len(args) == 3:
        start, end, step = args
        for i in iterable[iterable.index(start) : iterable.index(end) : step]:
            result_list.append(i)
        return result_list
