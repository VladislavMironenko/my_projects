import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time
import random


async def fetch_url(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.text()


async def adidas_func(size , gender):
    url = f'https://www.adidas.ua/{gender}/vzuttya/krosivki/{size}?page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url, headers)
        soup = BeautifulSoup(response, 'lxml')
        q = int(soup.find('div', class_="pagination__select").find('p', class_="common-text pagination__select--total").text.strip()[-1])
        print(f'Всего страниц: {q}')
        tasks = []

        for i in range(1, q + 1):
            URL = f'https://www.adidas.ua/{gender}/vzuttya/krosivki/{size}?page={i}'
            tasks.append(fetch_url(session, URL, headers))


        responses = await asyncio.gather(*tasks)

        lst = []
        res = []
        o=1
        for response in responses:
            soup = BeautifulSoup(response, 'lxml')
            r = soup.find('div', class_='list store__list')
            time.sleep(random.randint(1, 3))
            for s in r:
                ur_sale_price = s.find('div', class_="price__sale")
                if ur_sale_price is not None:
                    ur_sale_price = ur_sale_price.text.strip()
                    ur_price = s.find('div', class_="price__first").text.strip()
                    ur_title = s.find('div', class_="product__content").find('a', class_="product__info").find(
                        'span').text.strip()
                    ur_url = f'https://www.adidas.ua{s.find("a")["href"]}'.strip()
                    if ur_url not in lst:
                        lst.append(ur_url)
                        res.append({
                            'Модель': ur_title,
                            'Цена': ur_price,
                            'Цена со скидкой': ur_sale_price,
                            'Ссылка': ur_url
                        })
            print(f'{o}/{q}')
            o+=1
        with open('result_adidas_sneakers.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=4, ensure_ascii=False)

        print('Сбор информации завершен')


def main():
    asyncio.run(adidas_func('choloviki' , 9))


if __name__ == '__main__':
    main()