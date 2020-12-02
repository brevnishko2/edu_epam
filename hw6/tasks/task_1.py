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
from collections import defaultdict


def instances_counter(cls):
    """
    Append two methods and one attr:
    get_created_instances() - return class creation count
    reset_instances_counter() - return creation count and reset it
    __created_count - dict with class's and inheritor's created count.
    Parent and every new inheritor has it's own created count and
    don't increase other's created count.
        Args:
            cls: Any class
        Returns:
            Same class

    """
    cls.__created_count = defaultdict(int)

    @classmethod
    def get_instances(class_name):
        return cls.__created_count[class_name]

    @classmethod
    def reset_counter(class_name):
        prev_created_count = cls.__created_count[class_name]
        cls.__created_count[class_name] = 0
        return prev_created_count

    def decorator(func):
        def append_counter_to_new(*args, **kwargs):
            class_name = args[0]
            cls.__created_count[class_name] += 1
            result = func(class_name)
            return result

        return append_counter_to_new

    cls.__new__ = decorator(cls.__new__)
    cls.get_created_instances = get_instances
    cls.reset_instances_counter = reset_counter
    return cls
