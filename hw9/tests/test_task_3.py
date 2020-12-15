from pathlib import Path
from hw9.tasks.task_3 import universal_file_counter


path1 = Path.resolve(Path(__file__).parent)


def test_txt_counter():
    assert universal_file_counter(path1, "txt") == 13


def test_token_count():
    assert universal_file_counter(path1, "py", str.split) == 133


def test_another_token_count():
    assert universal_file_counter(path1, "py", str.strip) == 73


def test_count_all_files_lines():
    assert universal_file_counter(path1, "*") == 86
