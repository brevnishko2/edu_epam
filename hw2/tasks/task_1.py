"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    :param:
        file_path: path to working file
    :return:
        list: 10 longest words consisting from largest amount of unique symbols
    """
    dict_for_count_uniq = {}
    with open(file_path, encoding="unicode-escape") as inf:
        for line in inf:
            # make line without punctuation
            clean_line = line.translate(
                str.maketrans("", "", string.punctuation)
            ).split()
            # for every word in line count unique letters
            for word in clean_line:
                list_for_uniq = []
                for char in word:
                    if char not in list_for_uniq:
                        list_for_uniq.append(char)
                dict_for_count_uniq[word] = len(list_for_uniq)
    # get 10 longest
    result_list = [
        i[0]
        for i in sorted(dict_for_count_uniq.items(), reverse=True, key=lambda a: a[1])[
            :10
        ]
    ]
    return result_list


def get_rarest_char(file_path: str) -> str:
    """
    :param:
        file_path: path to working file
    :return:
        line: one or more rarest char
        example: 'char1 char2 char3 etc.'
    """
    dict_for_count = {}
    with open(file_path, encoding="unicode-escape") as inf:
        for line in inf:
            # make line without punctuation
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            # count every char
            for char in clean_line:
                if char in dict_for_count:
                    dict_for_count[char] += 1
                else:
                    dict_for_count[char] = 1
    # sort value in dict and find rarest chars
    result_list = sorted(dict_for_count.items(), key=lambda item: item[1])
    result_string = [char[0] for char in result_list if char[1] == result_list[0][1]]
    return " ".join(result_string)


def count_punctuation_chars(file_path: str) -> int:
    """
    :param:
        file_path: path to working file
    :return:
        int: punctuation's chars count
    """
    result = 0
    with open(file_path, encoding="unicode-escape") as inf:
        for line in inf:
            result += len([char for char in line if char in string.punctuation])
    return result


def count_non_ascii_chars(file_path: str) -> int:
    """
    :param:
        file_path: path to working file
    :return:
        int: non ascii char's count
    """
    with open(file_path, encoding="unicode-escape") as inf:
        result = 0
        for line in inf:
            for char in line:
                if char not in string.printable:
                    result += 1
        return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    :param:
        file_path: path to file
    :return:
        line: most common non ascii char for document
    """
    dict_for_count = {}
    with open(file_path, encoding="unicode-escape") as inf:
        for line in inf:
            # count every non-ascii char
            for char in line:
                if char not in string.printable and char != " ":
                    if char in dict_for_count:
                        dict_for_count[char] += 1
                    else:
                        dict_for_count[char] = 1
    # find most common char(s) in dict
    result_list = sorted(dict_for_count.items(), reverse=True, key=lambda item: item[1])
    result_string = [char[0] for char in result_list if char[1] == result_list[0][1]]
    return " ".join(result_string)
