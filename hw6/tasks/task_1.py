"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
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
    cls._created_count = 0

    def get_instances(*self):
        return cls._created_count

    def reset_counter(*self):
        _prev_created_count = cls._created_count
        cls._created_count = 0
        return _prev_created_count

    def append_counter_to_new(*args, **kwargs):
        cls._created_count += 1
        return object.__new__(cls)

    cls.__new__ = append_counter_to_new
    cls.get_created_instances = get_instances
    cls.reset_instances_counter = reset_counter
    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
    User.get_created_instances()  # 0
