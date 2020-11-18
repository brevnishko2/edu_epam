"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
"""


def fizzbuzz(n: int):
    """
    generate fizz-buzz numbers from 1 to N
    :param: N: range of working
    :return: generator
    """
    numbers = [i for i in range(n + 1)]
    fizz = [None] + ([None] * 2 + ["fizz"]) * (n + 1 // 3)
    buzz = [None] + ([None] * 4 + ["buzz"]) * (n + 1 // 5)
    fizz_buzz = [None] + ([None] * 14 + ["fizz buzz"]) * (n + 1 // 15)

    for i in range(1, n + 1):
        yield fizz_buzz[i] or fizz[i] or buzz[i] or str(numbers[i])
