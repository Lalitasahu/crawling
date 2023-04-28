import re
import requests
import pandas as pd
from lxml import html
from requests import Session
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def detailpage(url):
    r = s.get(url)
    tree = html.fromstring(r.text)
    title =''.join(tree.xpath('//h1//text()')).strip()
    Product_code =''.join(tree.xpath('//div[@class="product-info summary col-fit col entry-summary product-summary"]//div[@class="product-sku"]//text()'))
    price = ''.join(tree.xpath('//div[@class="price-wrapper"]//bdi//text()')).strip()
    description = ''.join(tree.xpath('//div[@class="accordion-inner"]//text()')).strip().replace('\n','').replace('\t','')
    images = '||'.join(tree.xpath('//div[@class="woocommerce-product-gallery__image slide"]//a/@href'))

    data = {'title':title,'Product_code':Product_code,'price':price,'description':description,'images':images}
    return data

alldata = []
def listpage():
    url = 'https://www.lasculpte.com.au/collections/shapewear/'
    nextpage = url
    while nextpage:
        r = s.get(nextpage)
        tree = html.fromstring(r.text)
        products=tree.xpath('//div[@class="col-inner"]')
        for product in products:
            links = ''.join(product.xpath('.//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href'))
            detail =  detailpage(links)
            d={'link':links}
            d.update(detail)
            alldata.append(d)
            print(alldata)
    if tree.xpath('//ul[@class="page-numbers nav-pagination links text-center"]//li//a[@class="next page-number"]/@href'):
        nextpage=tree.xpath('//ul[@class="page-numbers nav-pagination links text-center"]//li//a[@class="next page-number"]/@href')
        print(f'nextpage...{nextpage}.................')
    else:
        nextpage = False
listpage()
df = pd.DataFrame(alldata)
df.to_excel('l_w_x.xlsx',index=False)




 #dictionary update sequence element #0 has length 4; 2 is required