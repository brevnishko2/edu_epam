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
from __future__ import annotations
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

    def __init__(self, homework: Homework, solution: str, author: Student):
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:
    """Class for creating people.
    Args:
        last_name: person last name
        first_name: person first_name

    Attributes:
        last_name: person last name
        first_name: person first_name

    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """Born to do homework"""

    def do_homework(self, hw: Homework, solution: str) -> HomeworkResult:
        """Do homework if it's actual.
        Args:
            hw: Homework obj
            solution: some text for doing homework. It should be 5 char or longer.

        Returns:
            HomeworkResult obj if it still active

        Raises:
            DeadlineError if deadline missing

        """
        if hw.is_active():
            return HomeworkResult(hw, solution, self)
        raise DeadlineError("You are late")


class Teacher(Person):
    """Class for teachers. Can create homework, check student's homework
    and reset already checked list
    Class attributes:
        homework_done: dict with all homework already done

    Methods:
        create_homework
        check_homework
        reset_results

    """

    homework_done: defaultdict = defaultdict(list)

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
        Check if homework result is correct and append it to homework_done
        if it's not in it.
        Args:
            hw_result: HomeworkResult obj created by student

        Returns:
            bool: False - if homework incorrect or
            if this solution of hw have already been used

        """
        if len(hw_result.solution) < 5:
            return False

        for _items in Teacher.homework_done[hw_result.homework]:
            if hw_result.solution in _items.solution:
                return False
        # append new solution to dict
        Teacher.homework_done[hw_result.homework].append(hw_result)

    @staticmethod
    def reset_results(*homework):
        """
        Delete homework results. Delete all homeworks if homework not specified
        Args:
            homework: one Homework obj or empty list

        """
        if not homework:
            Teacher.homework_done = defaultdict(list)
        elif homework[0] in Teacher.homework_done:
            # delete homework's results
            del Teacher.homework_done[homework[0]]


class DeadlineError(Exception):
    def __init__(self, text):
        self.text = text
