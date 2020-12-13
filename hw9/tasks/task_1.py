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
from typing import List, Union, Iterator


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
            for line in inf.readlines():
                yield line.strip()

    iter1, iter2 = iter(get_value(file_list[0])), iter(get_value(file_list[1]))
    value1, value2 = next(iter1), next(iter2)
    stop = 0

    while True:
        try:
            # yield min value and get new from file
            if value1 > value2:
                yield value2
                stop = 1
                value2 = next(iter2)
            else:
                yield value1
                stop = 0
                value1 = next(iter1)
        except StopIteration:
            # if files have different length yield remaining values
            try:
                while True:
                    if stop:
                        yield value1
                        value1 = next(iter1)
                    else:
                        yield value2
                        value2 = next(iter2)
            except StopIteration:
                break
