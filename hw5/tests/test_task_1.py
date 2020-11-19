from hw5.tasks.task_1 import Homework, Teacher, Student

student = Student("Ivan", "Vasilev")


def test_hw_in_time():
    hw = Teacher.create_homework("some text", 7)

    assert student.do_homework(hw) == hw


def test_hw_not_in_time():
    hw = Teacher.create_homework("another text", 0)

    assert student.do_homework(hw) is None


def test_is_homework():
    hw = Teacher.create_homework("one more text", 3)

    assert isinstance(hw, Homework)
