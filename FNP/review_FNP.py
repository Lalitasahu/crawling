import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'


def review():
    url = 'https://www.fnp.com/gift/cute-love-gift?OCCASION_TAGS=propose-day&pos=5'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    

review()