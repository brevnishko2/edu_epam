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
    :param file_path: path to working file
    :type file_path: str
    :return: 10 longest words consisting from largest amount of unique symbols
    :rtype: list
    """
    with open(file_path, encoding="unicode-escape") as inf:
        some_dict = {}
        value_list = []
        result_list = []
        for line in inf:
            clean_line = line.translate(
                str.maketrans("", "", string.punctuation)
            ).split()
            for i in clean_line:
                list_for_uniq = []
                for j in i:
                    if j not in list_for_uniq:
                        list_for_uniq.append(j)
                some_dict[i] = len(list_for_uniq)
        for key, value in some_dict.items():
            value_list.append([value, key])
        ten_largest_list = sorted(value_list, reverse=True)[0:10]
        for i in ten_largest_list:
            result_list.append(i[1])
        return result_list


def get_rarest_char(file_path: str) -> str:
    """
    :param file_path: path to working file
    :type file_path: str
    :return: rarest(all in one string if there are more than 1) symbol for document
    :rtype: str
    """
    with open(file_path, encoding="unicode-escape") as inf:
        some_dict = {}
        value_list = []
        result_string = ""
        for line in inf:
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            for i in clean_line:
                if i in some_dict:
                    some_dict[i] += 1
                else:
                    some_dict[i] = 1
        for key, value in some_dict.items():
            value_list.append([value, key])
        for i in sorted(value_list, key=lambda a: a[0]):
            if i[0] == sorted(value_list, key=lambda a: a[0])[0][0]:
                result_string += str(i[1] + " ")
        return result_string.strip()


def count_punctuation_chars(file_path: str) -> int:
    """
    :param file_path: path to working file
    :type file_path: str
    :return: Count every punctuation char
    :rtype: int
    """
    with open(file_path, encoding="unicode-escape") as inf:
        result = 0
        for line in inf:
            result += len([x for x in line if x in "-:,.!?"])
        return result


def count_non_ascii_chars(file_path: str) -> int:
    """
    :param file_path: path to working file
    :type file_path: str
    :return: Count every non ascii char
    :rtype: int
    """
    with open(file_path, encoding="unicode-escape") as inf:
        result = 0
        for line in inf:
            for i in line:
                if i not in string.printable:
                    result += 1
        return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    :param file_path: path to file
    :type file_path: str
    :return: most common non ascii char for document
    :rtype: str
    """
    with open(file_path, encoding="unicode-escape") as inf:
        value_list = []
        some_dict = {}
        result_string = ""
        for line in inf:
            for i in line:
                if i not in string.printable and i != " ":
                    if i in some_dict:
                        some_dict[i] += 1
                    else:
                        some_dict[i] = 1
        for key, value in some_dict.items():
            value_list.append([value, key])
        for i in sorted(value_list, key=lambda a: a[0]):
            if i[0] == sorted(value_list, reverse=True, key=lambda a: a[0])[0][0]:
                result_string += str(i[1] + " ")
        return result_string.strip()
