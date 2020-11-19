"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
Write a test for that function using pytest library.
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run
"""


def read_magic_number(file_path: str) -> bool:
    """
        Reads the first line of the file.
    If first line is a number returns true if number in an interval [1, 3)*
    and false otherwise. Raises ValueError if first line not number.

        Args:
            file_path (): path to file

        Returns:
            bool: True if line is number from 1 to 3, False otherwise
    """
    with open(file_path) as inf:
        line = inf.readline().strip()
    # check if all char in line are numbers
    if line.isdigit():
        if 1 <= int(line) < 3:
            return True
        return False
    else:
        raise ValueError
