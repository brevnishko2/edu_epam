from hw4.tasks.task_5 import fizzbuzz


def test_fizzbuzz():
    actual_result = list(fizzbuzz(40))
    expected_result = [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizz buzz",
        "16",
        "17",
        "fizz",
        "19",
        "buzz",
        "fizz",
        "22",
        "23",
        "fizz",
        "buzz",
        "26",
        "fizz",
        "28",
        "29",
        "fizz buzz",
        "31",
        "32",
        "fizz",
        "34",
        "buzz",
        "fizz",
        "37",
        "38",
        "fizz",
        "buzz",
    ]

    assert actual_result == expected_result
