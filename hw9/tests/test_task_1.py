from pathlib import Path
from hw9.tasks.task_1 import merge_sorted_files


path1 = Path.resolve(Path(__file__).parent) / "file1.txt"
path2 = Path.resolve(Path(__file__).parent) / "file2.txt"
path3 = Path.resolve(Path(__file__).parent) / "file3.txt"


def test_merge():
    merged_list = []
    for i in merge_sorted_files([path1, path2, path3]):
        merged_list.append(i)

    assert merged_list == [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "81",
    ]
