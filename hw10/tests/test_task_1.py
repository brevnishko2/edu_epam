from mock import Mock
from pathlib import Path
from hw10.tasks.task_1 import AsyncParsingToJSON
from asynctest import CoroutineMock
import pytest


path1 = Path.resolve(Path(__file__).parent) / "page.html"
path2 = Path.resolve(Path(__file__).parent) / "page1.html"


@pytest.mark.asyncio
async def test_correct_info_collection():
    with open(path1) as inf:
        page_content = inf.read()
    with open(path2) as inf:
        co_info = inf.read()

    a = AsyncParsingToJSON()
    a.get_valute = Mock(return_value=70)
    a.get_page_content = CoroutineMock(return_value=page_content)
    a.get_company_info = CoroutineMock(return_value=co_info)
    task = await a.get_result(1)
    expected_result = {
        "co_code": "mmm",
        "co_name": "3M",
        "price": 174.68,
        "P/E": 20.12,
        "growth": 2.81,
        "potential profit": 68.49,
        "market_cap": 7258.23,
    }

    assert task[0] == expected_result
