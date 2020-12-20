from bs4 import BeautifulSoup
import requests
import concurrent.futures
import datetime
import asyncio
import aiohttp
from operator import itemgetter
import json


class ThreadParsingToJSON:
    def __init__(self):
        self.path = "https://markets.businessinsider.com"
        self.now = datetime.datetime.now()
        self.valute = self.get_valute()

    def get_page_content(self, i):
        end = f"/index/components/s&p_500?p={i}"
        return requests.get("".join([self.path, end])).text

    def get_co_info(self, link):
        return requests.get("".join([self.path, link])).text

    def convert_to_number(self, string):
        lst = []
        for char in string:
            if char.isdigit() or char == ".":
                lst.append(char)
        return float("".join(lst))

    def get_script_value(self, scripts):
        for script in scripts:
            if "low52weeks" in repr(script):
                index = repr(script).find("low52weeks")
                lowest = self.convert_to_number((repr(script)[index + 12 : index + 20]))
                index = repr(script).find("high52weeks")
                highest = self.convert_to_number(
                    (repr(script)[index + 13 : index + 20])
                )
        return f"{(highest - lowest):.{2}f}"

    def get_valute(self):
        path_cb = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
        request = requests.get(
            path_cb + "/".join(map(str, [self.now.day, self.now.month, self.now.year]))
        ).text
        soup = BeautifulSoup(request, "lxml")
        return float(
            soup.find("valute", id="R01235").find("value").text.replace(",", ".")
        )

    def get_co_information(self, link):
        soup = BeautifulSoup(self.get_co_info(link), "lxml")
        co_code = link[8 : link.find("-stock")]
        pe = (
            soup.find("div", id="snapshot")
            .find_all("div", class_="snapshot__data-item")[8]
            .text.split()[0]
        )
        profit = self.get_script_value(soup.find_all("script"))
        market_cap = (
            soup.find("div", id="snapshot")
            .find_all("div", class_="snapshot__data-item")[2]
            .text.split()[0][0:-2]
        )
        return co_code, float(pe), float(profit), float(market_cap.replace(",", ""))

    def get_result(self, page):
        result_list = []
        soup = BeautifulSoup(self.get_page_content(page), "lxml")
        table = soup.find("table", class_="table table-small")
        for line in table.find_all("tr")[1:]:
            link = line.find("td").find("a").get("href")
            price = float(line.find_all("td")[1].text.split("\n")[1].replace(",", ""))

            code, pe, profit, market_cap = self.get_co_information(link)

            result_list.append(
                {
                    "co_code": code,
                    "co_name": line.find("td").text.strip(),
                    "price": price,
                    "P/E": pe,
                    "growth": float(
                        line.find_all("td")[9].text.strip().split("\n")[1][:-1]
                    ),
                    "potential profit": profit,
                    "market_cap": float(f"{(market_cap * self.valute):.{2}f}"),
                }
            )
        return result_list

    def create_json(self):
        result = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(1, 11):
                futures.append(executor.submit(self.get_result, i))
            for future in concurrent.futures.as_completed(futures):
                result.extend(future.result())
        price = sorted(result, reverse=True, key=itemgetter("price"))[:10]
        pe = sorted(result, key=itemgetter("P/E"))[:10]
        growth = sorted(result, reverse=True, key=itemgetter("growth"))[:10]
        profit = sorted(result, reverse=True, key=itemgetter("potential profit"))[:10]
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


class AsyncParsingToJSON:
    def __init__(self):
        self.path = "https://markets.businessinsider.com"
        self.now = datetime.datetime.now()
        self.valute = self.get_valute()

    async def get_page_content(self, i):
        end = f"/index/components/s&p_500?p={i}"
        async with aiohttp.ClientSession() as session:
            async with session.get("".join([self.path, end])) as resp:
                html = await resp.text()
                return html

    async def get_company_info(self, link):
        async with aiohttp.ClientSession() as session:
            async with session.get("".join([self.path, link])) as resp:
                html = await resp.text()
                return html

    def convert_to_number(self, string):
        lst = []
        for char in string:
            if char.isdigit() or char == ".":
                lst.append(char)
        return float("".join(lst))

    def get_script_value(self, scripts):
        for script in scripts:
            if "low52weeks" in repr(script):
                index = repr(script).find("low52weeks")
                lowest = self.convert_to_number((repr(script)[index + 12 : index + 20]))
                index = repr(script).find("high52weeks")
                highest = self.convert_to_number(
                    (repr(script)[index + 13 : index + 20])
                )
        return f"{(highest - lowest):.{2}f}"

    def get_valute(self):
        path_cb = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
        request = requests.get(
            path_cb + "/".join(map(str, [self.now.day, self.now.month, self.now.year]))
        ).text
        soup = BeautifulSoup(request, "lxml")
        return float(
            soup.find("valute", id="R01235").find("value").text.replace(",", ".")
        )

    async def get_co_information(self, link):
        soup = BeautifulSoup(await self.get_company_info(link), "lxml")
        co_code = link[8 : link.find("-stock")]
        pe = (
            soup.find("div", id="snapshot")
            .find_all("div", class_="snapshot__data-item")[8]
            .text.split()[0]
        )
        profit = self.get_script_value(soup.find_all("script"))
        market_cap = (
            soup.find("div", id="snapshot")
            .find_all("div", class_="snapshot__data-item")[2]
            .text.split()[0][0:-2]
        )
        return co_code, float(pe), float(profit), float(market_cap.replace(",", ""))

    async def get_result(self, page):
        result_list = []
        soup = BeautifulSoup(await self.get_page_content(i=page), "lxml")
        table = soup.find("table", class_="table table-small")
        for line in table.find_all("tr")[1:]:
            link = line.find("td").find("a").get("href")
            price = float(line.find_all("td")[1].text.split("\n")[1].replace(",", ""))

            code, pe, profit, market_cap = await self.get_co_information(link)

            result_list.append(
                {
                    "co_code": code,
                    "co_name": line.find("td").text.strip(),
                    "price": price,
                    "P/E": pe,
                    "growth": float(
                        line.find_all("td")[9].text.strip().split("\n")[1][:-1]
                    ),
                    "potential profit": profit,
                    "market_cap": float(f"{(market_cap * self.valute):.{2}f}"),
                }
            )
        return result_list

    async def async_access(self):
        result = []
        result_lists = await asyncio.gather(*(self.get_result(i) for i in range(1, 11)))
        for lst in result_lists:
            result.extend(lst)
        return result

    async def print_to_json(self):
        result = await self.async_access()
        price = sorted(result, reverse=True, key=itemgetter("price"))[:10]
        pe = sorted(result, key=itemgetter("P/E"))[:10]
        growth = sorted(result, reverse=True, key=itemgetter("growth"))[:10]
        profit = sorted(result, reverse=True, key=itemgetter("potential profit"))[:10]
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
