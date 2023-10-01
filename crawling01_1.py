# 네이버증권 코스피 거래 상위 종목 크롤링 1

## TOP 100 종목

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

for data in soup.select('table > tr'):
    if len(data.select('td')) == 12:
        no = data.select_one('.no').text
        name = data.select_one('a,tltle').text
        price = data.select_one('.number').text
        print (no, name, price)