"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""
import functools
from typing import Callable


def save_func_name(original_func: Callable) -> Callable:
    """
    Decorator that saves function's __name__, __doc__ and link to original function.
    Args:
        original_func: decorated func that need to be saved

    Returns:
        decorated function

    """

    def new_func(decorator):
        def wrapped(*args, **kwargs):
            return decorator(*args, *kwargs)

        wrapped.__doc__ = original_func.__doc__
        wrapped.__name__ = original_func.__name__
        wrapped.__original_func = original_func
        return wrapped

    return new_func


def print_result(func):
    @save_func_name(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
