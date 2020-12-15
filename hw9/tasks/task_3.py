"""
Write a function that takes directory path, a file extension and
an optional tokenizer.
It will count lines in all files with that extension if there
are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Count lines in all files with that extension if there are
     no tokenizer. If a the tokenizer is not none,
     it will count tokens.
    Args:
        dir_path: working directory
        file_extension: file extension
        tokenizer: function that create tokens from string

    Returns:
        token_count: number of lines or tokens

    """
    token_count = 0

    def lines_counter(file_name, token=None):
        with open(file_name) as inf:
            count_lines = 0
            if not token:
                for _ in inf:
                    count_lines += 1
            else:
                for line in inf:
                    if isinstance(token(line), str):
                        count_lines += 1
                    else:
                        count_lines += len(token(line))
        return count_lines

    for file in dir_path.glob("*." + file_extension):
        token_count += lines_counter(file, tokenizer)
    return token_count
