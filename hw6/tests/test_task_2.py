from hw6.tasks.task_2 import Student, Teacher, HomeworkResult, DeadlineError

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_bad_value_homework_result():
    try:
        HomeworkResult(good_student, "fff", "Solution")
    except ValueError:
        assert True
    else:
        assert False


def test_homework_done():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_reset_result():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0


def test_hw_not_in_time():
    hw = Teacher.create_homework("Some text", 0)
    try:
        lazy_student.do_homework(hw, "very good solution")
    except DeadlineError:
        assert True
    else:
        assert False


def test_duplicated_solution():
    result_4 = good_student.do_homework(docs_hw, "I have done this hw")
    result_5 = lazy_student.do_homework(docs_hw, "I have done this hw")

    advanced_python_teacher.check_homework(result_4)
    advanced_python_teacher.check_homework(result_5)

    actual_result = len(Teacher.homework_done[docs_hw])

    assert actual_result == 1
