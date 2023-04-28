import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.cupshe.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.cupshe.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

params = {
    'seoUrl': 'dress',
    'pageNum': '1',
    'pageSize': '48',
    'brandId': '1',
    'channelId': '1',
    'terminalId': '1',
    'source': '2',
    'siteId': '1',
    'langCode': 'en-GB',
}
def crawl_detail(url):
    
    r=s.get(url)
    soup=bs(r.text,'html.parser')
    pro_id=soup.find('div',{'id':'mixpopup'}).get('productid')
    # for p in pro_id:
        # pro_api='https://cfs.cupshe.com/commodity/detail?lang=en-GB&currency=USD&countryCode=us&notFilterVedioFlag=false&thirdProductId='+str(p)+'brandId=1&channelId=1&terminalId=1&siteId=1'
    api_url = f'https://cfs.cupshe.com/commodity/detail?lang=en-GB&currency=USD&countryCode=us&notFilterVedioFlag=false&thirdProductId={pro_id}&brandId=1&channelId=1&terminalId=1&siteId=1'
    r=s.get(api_url,headers=headers)
    # soup=bs(r.text,'html.parser')
    print(r.url)
    js=r.json()
    # print(js)
    product=js['data']['commodities'][0]
    # for product in products:
    id=product.get('productId')
    image=product.get('medias')
    discription=product.get('description')
    return {
        'id':id,
        'image':image,
        'discription':discription
    }

all_data=[]
def crawl_list():
    response = requests.get('https://bff-shopify.cupshe.com/service/col/page', params=params, headers=headers)
    js=response.json()
    products=js['data']['dataDetail']
    # print(products)
    for i in products:
        product_url='https://www.cupshe.com/products/'+i.get('skcs')[0]['jumpPath']
        product_id=i.get('skcs')[0]['productId']
        detail=crawl_detail(product_url)
        d={'product_url':product_url,
            'product_id':product_id,
            'id':detail['id'],
            'image':detail['image'],
            'discription':detail['discription']
            }
        all_data.append(d)
        


# df=pd.DataFrame(all_data)
# df.to_excel('Cupshe.xlsx') 
crawl_list()
# all = crawl_detail('https://www.cupshe.com/products/shine-on-u-star-sweater-dress?_pos=1&_sid=99c0dbd94&_ss=r&variant=40181738340442')

print(all_data)