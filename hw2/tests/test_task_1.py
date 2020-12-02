"""
import os

from hw2.tasks.task_1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_longest_words():
    path = os.path.join(os.path.abspath
    (os.path.dirname(__file__)), "data.txt")
    actual_result = get_longest_diverse_words(path)

    assert actual_result == [
        "unmißverständliche",
        "Bevölkerungsabschub",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Fingerabdrucks",
        "Friedensabstimmung",
        "außenpolitisch",
        "Seinsverdichtungen",
        "Selbstbezichtigungen",
        "Vorausgeschickt",
    ]


def test_rarest_char():
    path = os.path.join(os.path.abspath
    (os.path.dirname(__file__)), "data.txt")
    actual_result = get_rarest_char(path)

    assert actual_result == "› ‹ Y é"


def test_punctuation_chars():
    path = os.path.join(os.path.abspath
    (os.path.dirname(__file__)), "data.txt")
    actual_result = count_punctuation_chars(path)

    assert actual_result == 3209


def test_count_non_ascii_chars():
    path = os.path.join(os.path.abspath
    (os.path.dirname(__file__)), "data.txt")
    actual_result = count_non_ascii_chars(path)

    assert actual_result == 1821


def test_most_common_non_ascii_char():
    path = os.path.join(os.path.abspath
    (os.path.dirname(__file__)), "data.txt")
    actual_result = get_most_common_non_ascii_char(path)

    assert actual_result == "ä"
"""
