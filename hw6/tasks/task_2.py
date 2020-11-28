"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


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

    def __init__(self, text: str, deadline: int):
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


class HomeworkResult:
    """
    Args:
        homework: Homework obj
        solution: some text as a solution for homework
        author: tuple(first_name, last_name) of student who doing homework
    Attributes:
        homework: Homework obj
        solution: some text as a solution for homework
        author: tuple(first_name, last_name) of student who doing homework
        created: time of obj creation

    """

    def __init__(self, homework: Homework, solution: str, author: tuple):
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class People:
    """Class for creating people.
    Args:
        last_name: person last name
        first_name: person first_name
    Attributes:
        last_name: person last name
        first_name: person first_name
    """

    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(People):
    """Inherited from People"""

    def do_homework(self, hw: Homework, solution: str) -> HomeworkResult:
        """Do homework if it's actual. Print "You are late" otherwise.
        Args:
            hw: Homework obj
            solution: some text for doing homework. It should be 5 char or longer.

        Returns:
            hw if it still active
            None otherwise

        """
        if hw.is_active():
            return HomeworkResult(hw, solution, (self.first_name, self.last_name))
        else:
            raise DeadlineError("You are late")


class Teacher(People):
    """Inherited from People
    Attributes:
        homework_done: dict with all homework already done

    """

    homework_done = defaultdict()

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Create Homework obj with text and deadline args
        Args:
            text: string
            deadline: datetime.timedelta

        Returns:
            Homework(text, deadline)
        """
        return Homework(text, deadline)

    def check_homework(self, hw_result: HomeworkResult):
        """
        Check if homework done correctly and append it to homework_done if it's not in it.
        Args:
            hw_result: HomeworkResult obj created by student
        Returns:
            bool: False - if homework incorrect or if this solution of hw have already been used

        """
        if len(hw_result.solution) < 5:
            return False
        if hw_result.homework in Teacher.homework_done:
            # check for recurring solution
            for _items in Teacher.homework_done[hw_result.homework]:
                if hw_result.solution in _items:
                    return False
            # append new solution to dict
            Teacher.homework_done[hw_result.homework].append(
                [hw_result.solution, hw_result.author]
            )
        else:
            Teacher.homework_done[hw_result.homework] = [
                [hw_result.solution, hw_result.author],
            ]

    @staticmethod
    def reset_results(*homeworks):
        """
        Delete homework results. Delete all homeworks if homework not specified
        Args:
            homeworks: one or list with Homework obj

        """
        if homeworks:
            # delete homeworks result
            for hw in homeworks:
                del Teacher.homework_done[hw]
        else:
            Teacher.homework_done = defaultdict()


class DeadlineError(Exception):
    def __init__(self, text):
        self.text = text
