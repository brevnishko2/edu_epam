"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str) -> bool:
    """Compare two string. Every '#' char is considered like backspace
    and delete prev char. A few '#' in a row means multiple delete
    Args:
        first: any string
        second: any string

    Returns:
        bool: True if after backspace strings are equal
              False otherwise

    """

    def clean_from_backspace(element: str) -> str:
        result_str = ""
        # if char not '#' append it to result string
        for char in element:
            if char != "#":
                result_str += char
            else:
                # Delete prev char from result string if char is '#'
                result_str = result_str[:-1]
        return result_str

    clean_first = clean_from_backspace(first)
    clean_second = clean_from_backspace(second)
    return clean_first == clean_second
