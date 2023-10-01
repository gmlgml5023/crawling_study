# 네이버증권 코스피 거래 상위 종목 크롤링 2

## TOP 100 중 전일 대비 상승 종목만 크롤링

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

print('< 전일 대비 상승 종목 > \n')

for data in soup.select('table > tr'):
    if (len(data.select('td')) == 12) & (data.select_one('span.red02') != None):
        no = data.select_one('.no').text
        name = data.select_one('a,tltle').text
        price = data.select_one('.number').text
        
        print (no, name, price)