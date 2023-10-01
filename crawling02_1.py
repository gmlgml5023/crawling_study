# 무신사 사이트 상의 카테고리 크롤링 1

## 첫페이지 크롤링 (브랜드명, 제품명, 가격)

import requests
from bs4 import BeautifulSoup

URL = 'https://www.musinsa.com/categories/item/001'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

for data in soup.select('div.section_product_list li.li_box'):
    brand = data.select_one('div > p.item_title > a').text
    name = data.select_one('div > p.list_info > a').attrs['title']
    price = data.select_one('div > p.price').text.strip().split('\n                ')[-1]
    
    print(f"브랜드 : {brand}\n제품명 : {name}\n가격 : {price}\n")