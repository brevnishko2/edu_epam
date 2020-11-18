"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
"""
import sys


def my_precious_logger(text: str):
    """
    write string to stderr if line starts with "error" and to the stdout otherwise
    :param text: any str text
    """
    if text[0:5] == "error":
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
