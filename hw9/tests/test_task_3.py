from pathlib import Path
from hw9.tasks.task_3 import universal_file_counter


path1 = Path.resolve(Path(__file__).parent)


def test_txt_counter():
    assert universal_file_counter(path1, "txt") == 7


def test_token_count():
    assert universal_file_counter(path1, "py", str.split) == 111


def test_count_all_files_lines():
    assert universal_file_counter(path1, "*") == 61
