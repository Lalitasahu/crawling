import requests
import re
from bs4 import BeautifulSoup as bs
from requests import Session
import pandas as pd
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def allUrl():
    url = 'https://shopcuup.com'
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    sublink = [i.find_all('a') for i in soup.find_all('ul','sub_sub_links')]
    for j in sublink:
        for k in j:
            # 9,10,19
            sub_link = 'https://shopcuup.com'+k.get('href')
            sub_link_name = k.text
            data = {
                'sub_link':sub_link,
                'sub_link_name':sub_link_name
            }
            # print(data)
            allurls.append(data)



def detailpage(row):

    # url = 'https://shopcuup.com/products/the-lurex-balconette-bundle'
    r = s.get(row['Pro_url'])
    price = re.search('price: "(.*?)",',r.text).group(1)
    compareAtPrice = re.search('compareAtPrice: "(.*?)",',r.text).group(1)
    try:
        title = re.search('titleRaw: "(.*?)",',r.text).group(1)
    except:
        title = ''

    try:
        Description = re.findall('description: "(.*?)\n',r.text)[0].replace('\\u003c','').replace('\\"1\\"\\u003e\\nul\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\n\\/ul\\u003e"','')
    except:
        Description = ''
    
    try:
        Fit_Details = re.findall('description: "(.*?)\n',r.text)[1].replace('\\u003c','').replace('\\"1\\"\\u003e\\nul\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\n\\/ul\\u003e"','')
    except:
        Fit_Details = ''
    
    try:
        Fabric_Care = re.findall('description: "(.*?)\n',r.text)[2].replace('\\u003c','').replace('\\"1\\"\\u003e\\nul\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\nli\\u003e','').replace('\\/li\\u003e\\n\\/ul\\u003e"','')
    except:
        Fabric_Care = ''
    
    data ={
        # 'landingpageUrl':row['pro_url'],
        'price':price,
        # 'compareAtPrice':compareAtPrice,
        # 'title':title,
        'Description':Description,
        'Fit_Details':Fit_Details,
        'Fabric_Care':Fabric_Care,
    }
    print(data)
    detailpagedata.append(data)


def listpage(row):
    r = s.get(row['sub_link'])
    cat_id = re.search('"rid":(.*?)};',r.text).group(1)
    brand_type = row['sub_link'].split('/')[-1].split('?')[0]
    page = 1
    begin = 56
    nextpage = True
    while nextpage:
        url = f'https://c22xk5.a.searchspring.io/api/search/search.json?userId=c5b7242c-c800-4cd4-8bb1-5e26edeea80a&domain=https://shopcuup.com/collections/{brand_type}?page={page}&siteId=c22xk5&page={page}&resultsPerPage={begin}&bgfilter.collection_id={cat_id}&redirectResponse=full&resultsFormat=native'
        r = s.get(url)
        js = r.json()
        if page >= js['pagination']['totalPages']:
            nextpage = False

        products = js['results']
        for i in products:
            name = i.get('name')
            id = i.get('id')
            brand = i.get('brand')
            price = i.get('price')
            pro_url = i.get('url')
            product_type = i.get('product_type')
            images = i.get('images')

            data = {
                'landingpageUrl':row['sub_link'],
                'Category':row['sub_link_name'],
                'name':name,
                'id':id,
                'brand':brand,
                'price':price,
                'Pro_url':pro_url,
                'product_type':product_type,
                'images':images
            }
            # print(data)
            listpagedata.append(data)

        page += 1
        # begin += 56

allurls = []
detailpagedata = []
listpagedata = []


df = pd.read_excel('shopcuup.xlsx').drop_duplicates(['id'])
for i in range(len(df)):
# for i in range(2):
    row = df.iloc[i].to_dict()
    detailpage(row)
df = pd.DataFrame(detailpagedata)
df.to_excel('detailpagedata.xlsx',index=False)


# df = pd.read_excel('Urls_all_cate.xlsx').drop_duplicates(['sub_link'])
# for i in range(len(df)):
# # for i in range(2):
#     row = df.iloc[i].to_dict()
#     listpage(row)
# df = pd.DataFrame(listpagedata)
# df.to_excel('shopcuup.xlsx', index=False)


# allUrl()
# df = pd.DataFrame(allurls)
# df.to_excel('Urls_all_cate.xlsx',index=False)