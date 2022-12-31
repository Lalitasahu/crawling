import requests 
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    '757659756236664b4e35': '0.9350493535834971',
    '725044574137426e4377': 'FpBZOwXv4OCoUfIEuiB5rpsu7AdyLxKVraXi3q4n2K90COmP62C02ZPouRxnWu, rwaAZPHi9ubATrno1fdpCXQYhPI5eFGRwT0Ix3qz8wf5195DeYhH3arLETbGbx',
    '68507174457178334b4b': 'upFzYGArYT5aPoPI9L9deqebif53DTZnh01rrbCG8hrbCG8haTQwf3',
    '_ffo': 'aHR0cHM6Ly93d3cuZWxram9wLm5v',
    '_fft': '181671786478827',
    'Origin': 'https://www.elkjop.no',
    'Connection': 'keep-alive',
    'Referer': 'https://www.elkjop.no/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'page': '1',
    'filter': 'BadgeUrl:/content/NO/layers/maanedens-gaming-deal.png',
    'sid': 'uvYub6fKN5rPDWA7BnCwhPqtEqx3KK',
    'log': 'cms',
    'format': 'json',
}
response = requests.get(
    'https://elkjop-prod.fact-finder.de/fact-finder/rest/v4/navigation/commerce_b2c_OCNOELK', params=params, headers=headers)

js = response.json()

alldata = []
products = js['hits']
for product in range(len(products)):
    Name = products[product].get('masterValues').get('Name')
    ProductURL = products[product].get('masterValues').get('ProductURL')
    ListPrice = products[product].get('masterValues').get('BeforePrice')
    SellingPrice =  products[product].get('masterValues').get('ChainPrice.Amount')
    Review = products[product].get('masterValues').get('AverageRating')
    TotalReviewCount = products[product].get('masterValues').get('TotalReviewCount')
    ProImage =  products[product].get('masterValues').get('Image')
    spcification = []
    Bullet1 = products[product].get('masterValues').get('Bulletpoint1')
    spcification.append(Bullet1)
    Bullet2 = products[product].get('masterValues').get('Bulletpoint2')
    spcification.append(Bullet2)
    Bullet3 = products[product].get('masterValues').get('Bulletpoint3')
    spcification.append(Bullet3)
    space = '||'.join(spcification)
    
    data = {
        'LandingPage':response.url,
        'ProductURL':ProductURL,
        'ProductRank': product,
        'Name':Name,
        'sellingPrice':SellingPrice,
        'ListPrice':ListPrice,
        'TotalReviewCount':TotalReviewCount,
        'Review':Review,
        'space':space,
        'ProImage':ProImage
    }
    alldata.append(data)
    
    print(alldata)
df = pd.DataFrame(alldata)
df.to_excel('elkjop.xlsx',index=False)