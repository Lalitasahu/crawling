import re
import requests
import pandas as pd
from lxml import html
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



def detailpage(url):
    r = s.get(url)
    # print(url,"....................................................")
    tree = html.fromstring(r.text)
    name = ''.join(tree.xpath('//div[@class="product-block product-block--header product-single__header small--hide"]//h1//text()'))
    description = "".join(tree.xpath('//div[@class="rte"]//text()')).strip()
    images = 'https:'+'||'.join(tree.xpath('//div[@class="product__thumb-item"]//a/@href'))
    try:
        price = tree.xpath('//span[@class="product__price"]//span//text()')[0]
    except:
        price = tree.xpath('//span[@class="product__price"]//span//text()')

    datas={
        'name':name,
        'description':description,
        'images':images,
        'price':price
    }
    # print(datas)
    
    return datas

allist = []
def listpage():
    url = 'https://www.curvyswimwear.com.au/collections/womens-swimwear-australia?filter.v.availability=1'
    nextpage=url
    while nextpage:
        r = s.get(nextpage)
        # print(url,"...............................................")
        tree = html.fromstring(r.text)
        products = tree.xpath('.//div[@class="grid-item__content"]')
        for product in products:
            link = 'https://www.curvyswimwear.com.au'+''.join(product.xpath('.//a[@class="grid-item__link"]/@href'))
            print(link)
            detail=detailpage(link)
            data={'link':link}
            data.update(detail)    
            allist.append(data)
            print(allist)
    if 'https://www.curvyswimwear.com.au'+''.join(tree.xpath('//a[@class="btn btn--large btn--circle btn--icon"]/@href')):
        nextpage = 'https://www.curvyswimwear.com.au'+''.join(tree.xpath('//a[@class="btn btn--large btn--circle btn--icon"]/@href'))
        print(f'next Page....{nextpage}..............................')
    else:
        nextpage = False


listpage()
df = pd.DataFrame(allist)
df.to_excel('Curvy_xpath.xlsx',index=False)