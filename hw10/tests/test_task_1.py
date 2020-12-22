from pathlib import Path

import pytest
from asynctest import CoroutineMock
from mock import Mock

from hw10.tasks.task_1 import NewParsing

path1 = Path.resolve(Path(__file__).parent) / "page.html"
path2 = Path.resolve(Path(__file__).parent) / "page1.html"


@pytest.mark.asyncio
async def test_correct_info_collection():
    with open(path1) as inf:
        page_content = inf.read()
    with open(path2) as inf:
        co_info = inf.read()

    a = NewParsing()
    a.get_conversion_rate = Mock(return_value=70)
    a.get_page_content = CoroutineMock(return_value=page_content)
    a.get_company_page = CoroutineMock(return_value=(co_info, 45.32))
    a.async_access = CoroutineMock(
        return_value=[
            ["/stocks/mmm-stock", "3.22"],
            ["/stocks/aos-stock", "17.67"],
            ["/stocks/abt-stock", "23.29"],
            ["/stocks/abbv-stock", "16.16"],
        ]
    )
    task1 = await a.get_companies_list(1)
    task2 = await a.get_companies_info()
    expected_result = {
        "name": "3M Co. ",
        "code": "MMM",
        "price": 13209.57,
        "profit": 68.49,
        "growth": 45.32,
        "P/E": 20.12,
    }

    assert task1[0] == ["/stocks/mmm-stock", "3.22"]
    assert task2[0] == expected_result
