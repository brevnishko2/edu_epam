from hw6.tasks.task_1 import instances_counter


@instances_counter
class ClassForTest:
    def __init__(self, *args):
        self.args = args


@instances_counter
class AnotherClass:
    pass


def test_class_counter():
    user, _, _ = ClassForTest(2, 3), ClassForTest(), ClassForTest(3)
    actual_result1 = ClassForTest.get_created_instances()
    expected_result1 = 3

    assert actual_result1 == expected_result1
    assert user.args == (2, 3)


def test_class_counter_reset():
    _, _, _, _ = [AnotherClass() for i in range(4)]
    actual_result = AnotherClass.reset_instances_counter()

    assert actual_result == 4
    assert AnotherClass.__created_count[AnotherClass] == 0
