import json
import requests
from bs4 import BeautifulSoup
import time
import random
import asyncio , aiohttp


async def fetch_url(session , url , headers):
    async with session.get(url = url , headers= headers) as response:
        return await response.text()

async def megasport_func(size , gender):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    }
    url = f'https://megasport.ua/ua/catalog/obuv/{gender}/page-1/?sizes%5B%5D={size}'
    async with aiohttp.ClientSession() as session:
        r = await fetch_url(session , url , headers)
        soup = BeautifulSoup(r , 'html.parser' )
        try:
            res = int(soup.find_all('option')[-1].text.strip()[-1])
        except:
            res = 1
        tasks = []
        for i in range(1 , res+1):
            URL = f'https://megasport.ua/ua/catalog/obuv/{gender}/page-{i}/?sizes%5B%5D={size}'
            tasks.append(fetch_url(session , URL , headers))
        responses = await asyncio.gather(*tasks)
        data = []
        o = 1
        for response in responses:
            soup = BeautifulSoup(response, 'html.parser')
            result = soup.find_all('div', class_="Z7K92d")
            time.sleep(random.randint(1, 3))
            for s in result:
                s_sale_price = s.find('span', class_="Wbzqvc")
                if s_sale_price != None:
                    s_url = f"https://megasport.ua{s.find('a')['href'].strip()}"
                    s_title = s.find('div' , class_="ihuxuw" ).text.strip('Ð³ÑÐ½').replace('Â' , '')[16:]
                    s_price = s.find('span' , class_="VIwf_b").text.strip('Ð³ÑÐ½').replace('Â' , '')
                    s_sale_price = s_sale_price.text.strip('Ð³ÑÐ½').replace('Â', '')
                    # s_title1 = html.unescape(s_title)
                    # print(s_title , s_price  , s_sale_price, s_url)
                    data.append({
                        'title' : s_title.replace('\xa0' , ''),
                        'price' : s_price.replace('\xa0' , ''),
                        'sale_price' : s_sale_price.replace('\xa0' , ''),
                        'url' : s_url.replace('\xa0' , '')
                    })
            print(f'{o}/{res}')
            o+=1
    with open('result_megasport_sneakers.json', 'w' , encoding='utf-8') as f:
        json.dump(data , f , indent=4 , ensure_ascii=False)
    print('Сбор инфорации завершен!')

def main():
    asyncio.run(megasport_func())
if __name__ == '__main__':
    main()

