import json
import requests
from bs4 import BeautifulSoup
import time
import random
import aiohttp ,asyncio


async def fetch_url(session , url , headers):
    async with session.get(url=url , headers=headers) as response:
        return await response.text()

async def megasport_shorts(size , gender):
    url = f'https://megasport.ua/ua/catalog/shorti/{gender}/page-1/?sizes%5B%5D={size}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    }

    async with aiohttp.ClientSession() as session:
        r = await fetch_url(session , url , headers)
        soup = BeautifulSoup(r , 'lxml')
        try:
            res1 = int(soup.find_all('option')[-1].text.strip()[-1])
        except:
            res1 = 1
        tasks = []
        for i in range(1 , res1+1):
            URL = f'https://megasport.ua/ua/catalog/shorti/{gender}/page-{i}/?sizes%5B%5D={size}'
            tasks.append(fetch_url(session , URL , headers))
        responses = await asyncio.gather(*tasks)
        lst = []
        o=1
        time.sleep(random.randint(1, 3))
        for response in responses:
            soup = BeautifulSoup(response, 'html.parser')
            res2 = soup.find_all('div' , class_="Z7K92d")
            for result in res2:
                result_sale_price = result.find('div', class_="vEwZcK").find('div', class_="loPig4").find('span', class_="Wbzqvc")
                if result_sale_price is not None:
                    result_title = result.find('div' , class_="vEwZcK").find('div' , class_="ihuxuw").text.strip('Ð³ÑÐ½').replace('Â' , '').replace('¨Ð¾ÑÑÐ¸ ' , '')
                    result_price = result.find('div' , class_="vEwZcK").find('div' , class_="loPig4").find('span' , class_="VIwf_b").text.strip('Ð³ÑÐ½').replace('Â' , '')
                    result_sale_price = result_sale_price.text.strip('Ð³ÑÐ½').replace('Â' , '')
                    result_url = f"https://megasport.ua{result.find('a')['href'].strip()}"
                    # print(result_url , "|" , result_title , "|" , result_price , "|" , result_sale_price)
                    lst.append({
                        'Модель': result_title.replace('\xa0', ''),
                        'Цена': result_price.replace('\xa0', ''),
                        'Цена со скидкой': result_sale_price.replace('\xa0', ''),
                        'Ссылка': result_url.replace('\xa0', '')
                    })
            print(f'{o}/{res1}')
            o+=1
    with open('result_megasport_shorts.json', 'w', encoding='utf-8') as file:
        json.dump(lst, file, indent=4, ensure_ascii=False)
    print('Сбор инфорации завершен!')
def main():
    asyncio.run(megasport_shorts())

if __name__ == '__main__':
    main()