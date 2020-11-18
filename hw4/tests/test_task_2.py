from mock import Mock
import requests
from hw4.tasks.task_2 import count_dots_on_i


def test_positive():
    requests.get = Mock()
    count_dots_on_i("awea")
    assert requests.get.called


def test_negative():
    requests.get = Mock(side_effect=ConnectionError)
    try:
        count_dots_on_i("awea")
    except ValueError:
        assert True
