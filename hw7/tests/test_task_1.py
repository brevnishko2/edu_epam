from hw7.tasks.task_1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {"simple_key": ["simple", "list", "of", "RED", "valued"]},
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": [1, "a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": ["RED", 1, 1.2],
}


def test_occurrence_count():
    actual_result1 = find_occurrences(example_tree, "RED")
    actual_result2 = find_occurrences(example_tree, "qwe")

    assert actual_result1 == 6
    assert actual_result2 == 0


def test_complex_element_in_dict():
    actual_result = find_occurrences(example_tree, ["RED", 1, 1.2])

    assert actual_result == 1


def test_find_int_and_float():
    actual_result1 = find_occurrences(example_tree, 1)
    actual_result2 = find_occurrences(example_tree, 1.2)

    assert actual_result1 == 2
    assert actual_result2 == 1
