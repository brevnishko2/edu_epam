"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
"""


def fizzbuzz(n: int):
    """
    Generator that takes a number N as an input
    and returns N FizzBuzz numbers
        Args:
            n ():range of working

        Returns:
            generator
    """
    numbers = [i for i in range(n + 1)]
    fizz = [""] + ([""] * 2 + ["fizz"]) * ((n + 3) // 3)
    buzz = [""] + ([""] * 4 + ["buzz"]) * ((n + 5) // 5)
    fizz_buzz = [""] + ([""] * 14 + ["fizz buzz"]) * ((n + 15) // 15)
    for i in range(1, n + 1):
        yield fizz_buzz[i] or fizz[i] or buzz[i] or str(numbers[i])
