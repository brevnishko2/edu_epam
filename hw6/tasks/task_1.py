"""
Написать декоратор instances_counter, который применяется к любому
классу и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров
класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """
    Append two methods and one attr:
    get_created_instances() - return class creation count
    reset_instances_counter() - return creation count and reset it
    _created_count - counter
        Args:
            cls: Any class
        Returns:
            Same class

    """
    cls.__created_count = 0

    @classmethod
    def get_instances(cls):
        return cls.__created_count

    @classmethod
    def reset_counter(cls):
        prev_created_count = cls.__created_count
        cls.__created_count = 0
        return prev_created_count

    def append_counter_to_new(*args, **kwargs):
        cls.__created_count += 1
        return super(cls, cls).__new__(cls)

    cls.__new__ = append_counter_to_new
    cls.get_created_instances = get_instances
    cls.reset_instances_counter = reset_counter
    return cls


@instances_counter
class User:
    pass


@instances_counter
class ClassForTest:
    def __init__(self, *args):
        self.args = args
