
import requests
import re
from lxml import html
from requests import Session
s = Session()
s.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0'}


def listpage():
    url = 'https://www.anomalyhaircare.com/shop'
    r = s.get(url)

    Title = re.findall("name: '(.*?)',",r.text)
    Product_link = re.findall("link: '(.*?)',",r.text)
    try:
        short_Des = re.findall("shortDesc: `(.*?)`,",r.text)
    except:
        short_Des = re.findall("shortDesc: '(.*?)',",r.text)
    longDescription =  re.findall("longDesc: `(.*?)`,",r.text)
    price = re.findall("price: '(.*?)',",r.text)
    image = re.findall("image: '(.*?)',",r.text)
    image2 = re.findall("image2: '(.*?)',",r.text)
    image2m = re.findall("image2m: '(.*?)',",r.text)
    longshadwo = re.findall("longShadowSmall: '(.*?)',",r.text)

    data = {
        'Title':Title,
        'Product_link':Product_link,
        'short_Des':short_Des,
        'longDescription':longDescription,
        'price':price,
        'image':image,
        'image2':image2,
        'image2m':image2m,
        'longDescription':longDescription
    }
    print(data)
    
listpage()


