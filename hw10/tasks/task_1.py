import asyncio
import json
import re
from operator import itemgetter
from typing import Dict, List, Tuple

import aiohttp
import requests
from bs4 import BeautifulSoup


class NewParsing:
    """Takes data from https://markets.businessinsider.com and create 4
    json files with top-10 companies in:
    - 1-year growth;
    - P/E
    - stock price (conv to rub)
    - difference(profit) between 52 weeks highest and lowest stock price

    """

    def __init__(self):
        self.path = "https://markets.businessinsider.com"
        self.conversion_rate = self.get_conversion_rate()

    def get_conversion_rate(self) -> float:
        """Takes current conversion rate rub to dollar
        Returns:
            float: 1 dollar price

        """
        path_cb = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = requests.get(path_cb).text
        soup = BeautifulSoup(response, "lxml")
        return float(
            soup.find("valute", id="R01235").find("value").text.replace(",", ".")
        )

    def get_script_value(self, script: str) -> float:
        """Find 52 weeks lowest and highest value in script code.
        Args:
            script: first script from soup.find("div", id="snapshot")

        Returns:
            profit: difference between highest and lowest price

        """
        value = re.search(r"low52weeks: (\d*.\d*)", script)
        low = float(value.group().split()[1].replace(",", ""))
        value = re.search(r"high52weeks: (\d*.\d*)", script)
        high = float(value.group().split()[1].replace(",", ""))
        return high - low

    async def get_page_content(self, i) -> str:
        """Takes html-code of page
        Args:
            i: page number

        Returns:
            html: page's html-code

        """
        end = f"/index/components/s&p_500?p={i}"
        async with aiohttp.ClientSession() as session:
            async with session.get("".join([self.path, end])) as resp:
                html = await resp.text()
                return html

    async def get_company_page(self, link) -> Tuple[str, str]:
        """Takes html-code of page
        Args:
            link ():

        Returns:
            tuple: html-code and company's growth

        """
        async with aiohttp.ClientSession() as session:
            async with session.get("".join([self.path, link[0]])) as resp:
                html = await resp.text()
                return html, link[1]

    async def get_companies_list(self, page) -> List[List]:
        """Collect ref of all companies pages from page into one list.
        Also collect 1-year growth of company
        Args:
            page: number of page

        Returns:
            companies_list: list with refs

        """
        companies_list = []
        soup = BeautifulSoup(await self.get_page_content(i=page), "lxml")
        table = soup.find("table", class_="table table-small")
        for line in table.find_all("tr")[1:]:
            link = line.find("td").find("a").get("href")
            growth = line.find_all("td")[9].text.strip().split("\n")[1][:-1]
            companies_list.append([link, growth])
        return companies_list

    async def async_access(self) -> List[List]:
        """Some async magic to make get_companies_list() faster.
        Collect refs from 1-10 site's pages
        Returns:
            result: list with refs

        """
        result = []
        result_lists = await asyncio.gather(
            *(self.get_companies_list(i) for i in range(1, 11))
        )
        for lst in result_lists:
            result.extend(lst)
        return result

    async def get_companies_info(self) -> List[Dict]:
        """Takes html-code of all companies and collect following
        company's info into a dict:
        - name
        - code
        - 1-year growth
        - stock price
        - profit
        - P/E
        Returns:
            result: list of dicts

        """
        result_list = []
        temp_result = await asyncio.gather(
            *(self.get_company_page(link) for link in await self.async_access())
        )
        for company in temp_result:
            soup = BeautifulSoup(company[0], "lxml")
            growth = float(company[1])
            table_with_name = soup.find("div", class_="price-section__row")
            name = table_with_name.find("span", class_="price-section__label").text
            code = (
                table_with_name.find("span", class_="price-section__category")
                .find("span")
                .text.split()[1]
            )
            table_with_price = soup.find("div", class_="price-section__values")
            price = float(
                table_with_price.find(
                    "span", class_="price-section__current-value"
                ).text.replace(",", "")
            )
            snapshot = soup.find("div", id="snapshot")
            profit = self.get_script_value(snapshot.find("script").decode())
            try:
                pe = float(
                    snapshot.find("div", class_="snapshot__header", text="P/E Ratio")
                    .parent.text.split()[0]
                    .replace(",", "")
                )
            except AttributeError:
                continue
            result_list.append(
                {
                    "name": name,
                    "code": code,
                    "price": round(price * self.conversion_rate, 2),
                    "profit": round(profit, 2),
                    "growth": growth,
                    "P/E": pe,
                }
            )
        return result_list

    def start(self):
        """final action that takes all data and create 4 top-10
        json files.

        """
        result = list(asyncio.run(self.get_companies_info()))
        price = sorted(result, reverse=True, key=itemgetter("price"))[:10]
        pe = sorted(result, key=itemgetter("P/E"))[:10]
        growth = sorted(result, reverse=True, key=itemgetter("growth"))[:10]
        profit = sorted(result, reverse=True, key=itemgetter("profit"))[:10]
        top_10 = [price, pe, growth, profit]
        names_for_files = [
            "top_10_price",
            "top_10_pe",
            "top_10_growth",
            "top_10_profit",
        ]
        for i in range(len(top_10)):
            with open(f"{names_for_files[i]}.json", "w") as ouf:
                ouf.write(json.dumps(top_10[i], indent=4))


if __name__ == "__main__":
    instance = NewParsing()
    instance.start()
