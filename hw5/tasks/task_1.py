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
    """
    Args:
        text: text for homework task
        deadline: time since creation, when homework become inactive
    Attributes:
        text: text for homework task
        deadline: time since creation, when homework become inactive
        created: time of obj creation

    """

    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Check if homework still actual
        Returns:
            True if deadline hasn't come yet
            False otherwise

        """
        return (datetime.datetime.now() - self.created) < self.deadline


class Student:
    """
    Args:
        last_name: last name of the student
        first_name: first name of the student
    Attributes:
        last_name: last name of the student
        first_name: first name of the student

    """

    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, hw: Homework) -> Homework or None:
        """Do homework if it's actual. Print "You are late" otherwise.
        Args:
            hw: Homework obj

        Returns:
            hw if it still active
            None otherwise

        """
        if hw.is_active():
            return hw
        else:
            print("You are late")
            return None


class Teacher:
    """
    Args:
        last_name: last name of the teacher
        first_name: first name of the teacher
    Attributes:
        last_name: last name of the teacher
        first_name: first name of the teacher
    """

    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: datetime.timedelta) -> Homework:
        """Create Homework obj with text and deadline args
        Args:
            text: string
            deadline: datetime.timedelta

        Returns:
            Homework(text, deadline)
        """
        return Homework(text, deadline)
