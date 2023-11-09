import json
import requests
from bs4 import BeautifulSoup
import time
import random
import asyncio , aiohttp


async def fetch_url(session , url , headers):
    async with session.get(url=url , headers= headers) as response:
        return await response.text()


async def adidas_shorts_run(size , gender):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url = f'https://www.adidas.ua/{gender}/odyag/shorti/{size}?page=1'
    async with aiohttp.ClientSession() as session:
        s = await fetch_url(session , url , headers)
        soup = BeautifulSoup(s , 'html.parser')
        try:
            q = int(soup.find('div',class_="pagination__select").find('p' , class_="common-text pagination__select--total").text.strip()[-1])
        except:
            q=1

        print(f'Всего страниц : {q}')
        tasks = []
        for i in range(1 , q+1):
            URL = f'https://www.adidas.ua/{gender}/odyag/shorti/{size}?page={i}'
            tasks.append(fetch_url(session , URL , headers))
        responses = await asyncio.gather(*tasks)


        lst = []
        o=1
        for response in responses:
            soup = BeautifulSoup(response, 'html.parser')
            r = soup.find('div' , class_="list store__list")
            time.sleep(random.randint(1,3))
            for result in r:
                result_sale_price = result.find('div', class_="price__sale")
                if result_sale_price is not None:
                    result_title = result.find('a' , class_="product__info").find('span').text.strip()
                    result_sale_price = result_sale_price.text.strip()
                    result_price = result.find('div', class_="price__first").text.strip()
                    result_url = f"https://www.adidas.ua{result.find('a')['href'].strip()}"
                    lst.append({
                        'Модель' : result_title,
                        'Цена' : result_price,
                        'Цена со скидкой' : result_sale_price,
                        'Ссылка' : result_url
                    })
            print(f'{o}/{q}')
            o+=1
    with open('result_adidas_shorts.json', 'w' , encoding='utf-8') as f:
        json.dump(lst , f , indent=4 , ensure_ascii=False)
    print('Сбор информации завершен')
def main():
    asyncio.run(adidas_shorts_run('zhinki'))

if __name__ == '__main__':
    main()