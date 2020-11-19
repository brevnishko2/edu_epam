"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """
        check if homework steel actual
        Returns:
            bool: True if datetime.now - creation time < deadline
                False otherwise
        """
        return (datetime.datetime.now() - self.created) < self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, hw: Homework) -> Homework or None:
        """
        Args:
            hw (): Homework obj

        Returns:
            hw if it steel active
            None otherwise
        """
        if hw.is_active():
            return hw
        else:
            print("You are late")
            return None


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: datetime.timedelta) -> Homework:
        """
        create Homework obj with text and deadline args
        Args:
            text (): string
            deadline (): datetime.timedelta

        Returns:
            Homework(text, deadline)
        """
        return Homework(text, deadline)
