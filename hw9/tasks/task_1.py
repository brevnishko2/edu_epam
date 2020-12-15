"""
Write a function that merges integer from sorted files and returns an
 iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator, Tuple
import heapq
from random import random


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge 2 files and return iterator. If files have eq values in
    the same lines returns both values one by one.
    Args:
        file_list: path to files

    Returns:
        iterator: yield sorted values from merged files

    """

    def get_value(file: Union[Path, str]) -> Iterator:
        with open(file) as inf:
            for line in inf:
                yield int(line.strip())

    queue: List[Tuple[int, float, Iterator]] = []
    for file in file_list:
        iterator = iter(get_value(file))
        heapq.heappush(queue, (next(iterator), random(), iterator))
    while True:
        try:
            next_value = (next(queue[0][2]), random(), queue[0][2])
            heapq.heappush(queue, next_value)
        except (StopIteration, IndexError):
            pass
        try:
            value_for_return = heapq.heappop(queue)
            yield str(value_for_return[0])
        except IndexError:
            break
