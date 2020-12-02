"""
Given an array of size n, find the most common and the
least common elements.
The most common element is the element that appears
more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import Dict, List, Tuple


def major_and_minor_elem(inp: List[int]) -> Tuple[int, int]:
    """
    :param inp: array is non-empty and the most common element
    always exist in the array
    :return: Tuple(least_common_elem, most_common_elem)
    """
    value_count_dict: Dict[int, int] = {}
    for value in inp:
        if value in value_count_dict:
            value_count_dict[value] += 1
        else:
            value_count_dict[value] = 1
    return (
        max(value_count_dict.items(), key=lambda item: item[1])[0],
        min(value_count_dict.items(), key=lambda item: item[1])[0],
    )
