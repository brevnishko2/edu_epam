"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Count every element occurrence in dict
    Args:
        tree: any dict
        element (): any element to count
        counter: inner arg to count occurrences

    Returns:
        element's occurrence count

    """
    counter = 0
    if isinstance(tree, dict):
        if element in tree.values():
            counter += 1
        for value in tree.values():
            counter += find_occurrences(value, element)
    elif isinstance(tree, (set, list, tuple)):
        if element in tree:
            counter += 1
        for item in tree:
            counter += find_occurrences(item, element)
    return counter
