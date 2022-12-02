import re
import pandas as pd
import requests 
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
url = 'https://www.21faves.com/products/padded-tied-contrast-color-falbala-halterneck-three-pieces-set?spm=..collection_3ba3880c-30e7-4846-bc11-6d555c652549.collection_detail_1.2&spm_prev=..product_64695e08-72a4-4383-84da-4947b6bcba74.header_1.1'
r = s.get(url)
tree = html.fromstring(r.text)
title = "".join(tree.xpath('//h1/text()'))
price = ''.join(tree.xpath('//span[@class="product-info__header_price dj_skin_product_detail_price money"]//text()')).strip()
# speci_key = tree.xpath('//table//tbody//tr//td]')
spaci_key = "".join(tree.xpath('//table//tbody//tr//td[@style="width:25%"]/text()'))
spaci_value = "".join(tree.xpath('//table//tbody//tr//td[@style="width:45%"]/text()'))
particuler =  "".join(tree.xpath('//table//tbody//tr//td[@style="width:25%" and contains(string(),"Sku")]//following-sibling::td//text()'))
specification={}
for i in spaci_key:
    for j in spaci_value:
        specification[i]:specification[j]

data={
    'title':title,
    'price':price,
    'spaci_key':spaci_key,
    'spaci_value':spaci_value,
    'particuler':particuler,
}
print(data)
specification.update(data)