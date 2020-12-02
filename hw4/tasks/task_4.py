"""
Write a function that takes a number N as an input and returns N
FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

Instruction:
    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository <path your repository>
    - Checkout branch <your branch>
    - Open terminal
    - Write "python -m doctest -v <path to your file.py>"
    - Congratulations!
"""
from typing import List


def fizzbuzz(limit: int) -> List[str]:
    """
        Takes a number N as an input and returns N FizzBuzz numbers
        Args:
            limit (): range of working

        Returns:
            result_list: list with str(number) or fizz/buzz from 1 to N
        examples:
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(-5)
    []
    """
    result_list = []
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 != 0:
            result_list.append("fizz")
        elif number % 5 == 0 and number % 3 != 0:
            result_list.append("buzz")
        elif number % 5 == 0 and number % 3 == 0:
            result_list.append("fizz buzz")
        else:
            result_list.append(str(number))
    return result_list
