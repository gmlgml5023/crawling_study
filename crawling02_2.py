# 무신사 사이트 상의 카테고리 크롤링 2

## 첫페이지 크롤링 (브랜드명, 제품명, 가격)

import requests
from bs4 import BeautifulSoup

URL = 'https://www.musinsa.com/categories/item/001'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

for page in range(1,11):
    URLS = f"https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page={page}&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure="
    res = requests.get(URLS)
    soup = BeautifulSoup(res.text, 'html.parser')
    print("-------------------------------------")
    print(f"{page}페이지\n")
    
    for data in soup.select('div.section_product_list li.li_box'):
        brand = data.select_one('div > p.item_title > a').text
        name = data.select_one('div > p.list_info > a').attrs['title']
        price = data.select_one('div > p.price').text.strip().split('\n                ')[-1]
        
        print(f"브랜드 : {brand}", f"\n제품명 : {name}", f"\n가격 : {price}\n")