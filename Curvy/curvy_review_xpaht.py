import re
import requests
import pandas as pd
from lxml import html
from requests import Session
s = Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.curvyswimwear.com.au',
    'Connection': 'keep-alive',
    'Referer': 'https://www.curvyswimwear.com.au/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'productId': '2254278000736',
    'productName': 'Chlorine Resistant Black 3/4 Swim Pant',
    'productType': 'Swim Bottoms',
    'productSKU': 'chlorine-resistant-black-3-4-pant',
    'page': '2',
    'apiKey': 'pubkey-0jdtFX2998spLs54i35084WdAq8Ql3',
    'storeUrl': 'curvyswimwear.myshopify.com',
    'take': '5',
    'sort': 'recent',
    'widgetLanguage': 'en',
}


def get_parms(url):
    r = s.get(url)
    tree = html.fromstring(r.text)
    prd_id = re.search('item_id: "(.*?)",',r.text).group(1)
    prd_name = re.search('item_name: "(.*?)",',r.text).group(1)
    productType =  re.search("item_category: '(.*?)',",r.text).group(1)
    productSKU=re.search('"handle":"(.*?)",',r.text).group(1)
    apiKey = ''.join(tree.xpath('//script[@id="stamped-script-widget"]/@data-api-key'))
    storeUrl = re.search('shop=(.*?)"',r.text).group(1)
    return {
        'productId': prd_id,
        'productName': prd_name,
        'productType': productType,
        'productSKU': productSKU,
        # 'page': '1',
        'apiKey': apiKey,
        'storeUrl': storeUrl,
        'take': '5',
        'sort': 'recent',
        'widgetLanguage': 'en',
    }

allreviews = []
def review_with_xpath(row):
    # while nextpage:
        url = row['link']
        print(url)
        params = get_parms(url)
        # params['page'] = '4'
        response = requests.get('https://stamped.io/api/widget', params=params, headers=headers)
        print(response)
        js = response.json()
        tree = html.fromstring(js['widget'])
        # print(tree)
        userName = tree.xpath('//strong[@class="author"]//text()')# list conver into with join ||
        title = tree.xpath('//h3//text()')
        reviews = tree.xpath('//p[@class="stamped-review-content-body"]//text()')
        Date = tree.xpath('//div[@class="created"]//text()')
        for UN,T,R,D in zip(userName,title,reviews,Date):
            d={'userName':UN,'title':T,'reviews':R,'Date':D,'Pro_URL':url}
            print(d)
            allreviews.append(d)
    # if nextpage = 



df = pd.read_excel('Curvy_xpath.xlsx')
for i in range(len(df)):
# for i in range(1):
    row = df.iloc[i].to_dict()
    review_with_xpath(row)

df = pd.DataFrame(allreviews)
df.to_excel('curvy_review.xlsx',index=False)