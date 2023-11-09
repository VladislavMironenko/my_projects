from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup
import random
import json



async def puma_shorts(size , gender):
    url = f'https://ua.puma.com/ru/{gender}/odezhda/shorty.html?size={size}'
    option = Options()
    option.add_argument('--headless')
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    try:
        driver.get(url=url)
        # time.sleep(5)
        # driver.find_element(By.CLASS_NAME, 'sorter-item__text').click()
        # b = driver.find_element(By.CLASS_NAME, 'catalog-pager')
        # action = ActionChains(driver)
        # action.move_to_element(b).perform()
        # bvv = driver.find_element(By.CLASS_NAME, 'btn.btn_white.btn-pager.js-load-more')
        # bvv.click()
        # time.sleep(10)
        # driver.implicitly_wait(20)
        # scroll = 50
        print('Начало')
        result = []
        while True:
            try:
                # driver.execute_script(f'window.scrollBy(0, {scroll});')
                # # time.sleep(3)
                # s = driver.find_element(By.CLASS_NAME , "btn.btn_white.btn-pager.js-load-more")
                # action = ActionChains(driver)
                # action.move_to_element(s).perform()
                b = driver.find_element(By.CLASS_NAME, 'catalog-pager')
                action = ActionChains(driver)
                action.move_to_element(b).perform()
                bvv = driver.find_element(By.CLASS_NAME, 'btn.btn_white.btn-pager.js-load-more')
                bvv.click()
                time.sleep(10)
                try:
                    driver.find_element(By.CLASS_NAME , 'subscribe-promo-popup__inner-container')
                    b = driver.find_element(By.CLASS_NAME , 'eins-modal-close.subscribe-promo-popup__close')
                    b.click()
                    time.sleep(2)
                except:
                    continue
            except:
                res = driver.find_elements(By.CLASS_NAME, 'grid__item.image-mod01')
                # time.sleep(random.randint(1, 3))
                for r in res:
                    r_price_sale = r.find_element(By.CLASS_NAME, 'old-price.sly-old-price.no-display').text.strip()
                    r_title = r.find_element(By.CLASS_NAME, 'product-item__name').text.strip()
                    r_price = r.find_element(By.CLASS_NAME, 'special-price').text.strip()
                    r_url = r.find_element(By.TAG_NAME, 'a').get_attribute('href').strip()
                    result.append({
                        'Модель': r_title.replace('\xa0', ''),
                        'Цена': r_price.replace('\xa0', ''),
                        'Цена со скидкой': r_price_sale.replace('\xa0', ''),
                        'Ссылка': r_url
                    })
                with open('result_puma_shorts.json', 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=4, ensure_ascii=False)
                return 'Финишь'
                # driver.close()
                # driver.quit()

    except Exception as e:
        print("Ошибка:", e)
    finally:
        driver.close()
        driver.quit()

def main():
    puma_shorts()

if __name__ == '__main__':
    main()