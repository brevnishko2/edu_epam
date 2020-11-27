from hw5.tasks.task_2 import print_result
import functools


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


@print_result
def some_func():
    """Returning some very important data"""
    return "some data"


def test_data_saving():
    expecting_name = "custom_sum"
    expecting_doc = "This function can sum any objects which have __add___"
    actual_name = custom_sum.__name__
    actual_doc = custom_sum.__doc__
    original_func = custom_sum.__original_func

    assert actual_doc == expecting_doc
    assert actual_name == expecting_name
    assert str(original_func).startswith("<function custom_sum at ")


def test_another_func():
    expecting_name = "some_func"
    expecting_doc = "Returning some very important data"
    actual_name = some_func.__name__
    actual_doc = some_func.__doc__
    original_func = some_func.__original_func

    assert actual_doc == expecting_doc
    assert actual_name == expecting_name
    assert str(original_func).startswith("<function some_func at ")
