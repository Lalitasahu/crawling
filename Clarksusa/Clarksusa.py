import requests 
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
# url = 'https://www.clarksusa.com/womens/all-styles/c/w2'


cookies={
    'akacd_holding_page_us': '3850876434~rv=2~id=6ee4f1f959482a5ec90e7240e2e6c2d8',
    'mt.v': '2.1740891838.1673423462042',
    '_gcl_au': '1.1.1494067051.1673423463',
    '_ga_W2ST5RZJDR': 'GS1.1.1673431271.2.1.1673432784.0.0.0',
    '_ga': 'GA1.1.1101104015.1673423464',
    'cmTPSet': 'Y',
    'CoreID6': '48276771176716734234639&ci=52540000|www.clarksusa.com',
    '52540000|www.clarksusa.com_clogin': 'v=1&l=17258241673431272294&e=1673434514398',
    '_li_dcdm_c': '.clarksusa.com',
    '_lc2_fpi': 'b5bb2b35bd9c--01gpfwz9p0fc9dsnxvnma53w0p',
    'JSESSIONID': '2DEB4C0160A779194A88891826C775C2.c2',
    'ROUTEID': '.2',
    'b1pi': '!0FWLPWuSh/5/FgTohS0euLFGMEo7Rm7VQ7XD/XiWE5ZJ+tInfXSN7qXMRRtFgsdjwhcNLesDfp28qto=',
    '_cs_c': '0',
    '_cs_id': '6541acb5-4662-af9b-8613-c3c5fec5ea64.1673423464.3.1673432712.1673431229.1.1707587464465',
    'REVLIFTER': '{"w":"fe93176c-afed-4170-aba7-cdeb8342c252","u":"7c480fdd-efe8-4415-8f94-a17957ffc3b8","s":"28a8972a-c3b4-4bf6-9460-dd0dbbd3b143","se":1676015464}',
    '_pin_unauth': 'dWlkPU9EQmpPRFF6Tm1RdFlURTBPQzAwWVRVNExXRXdZelV0WmpZMU0yVXhPVEl6WVdWag',
    '_gid': 'GA1.2.769882816.1673423466',
    'RT': '"z=1&dm=www.clarksusa.com&si=ad4fef99-7710-4f09-8367-759cb083a281&ss=lcrhso7x&sl=a&tt=g03&obo=8&rl=1"',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNjczNDIzNDY2NzAwLFwidW9cIjoxNjczNDIzNDY2NzAwLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjBkZDExNzg2M2JhZjQ0NmM5ZGVkNTk0NmMwMzBjYTdkXCJ9In0=',
    'tpc_a': 'c8b1ed17629943ccb81b61de44d3f5a1.1673423466.52i.1673431319',
    '__attentive_id': '0dd117863baf446c9ded5946c030ca7d',
    '__attentive_cco': '1673423466703',
    '_fbp': 'fb.1.1673423467712.705983757',
    '__attentive_dv': '1',
    'CMAVID': 'none',
    'clarkscookiepolicy': 'accept',
    'ADRUM': 's=1673432783546&r=https%3A%2F%2Fwww.clarksusa.com%2Fwomens%2Fall-styles%2Fc%2Fw2%3F893600741',
    'BVImplmain_site': '19244',
    'a1ashgd': '2lrk6phpjrj000002lrk6phpjrj00000',
    'BVBRANDID': '84180b92-801a-4c06-bf65-7095220ddd68',
    'cto_bundle': 'V_kfk19ROWtVZG0zWHdqVXd0MmdyZzlRU3FpN2RzOUJLOXo3SnkxNVRhUkFCbXEwT1RpUjlacGclMkZxeG50YXR6ajFZMFJ3TkdSVng0TGRBZW55WjFhakFya3c0UWxSdmhybzN3aTZqQyUyQjNwdkdCaTI0ZXgzNXR4WEZzUTI3a0VXRSUyRlp4SE42ZmJnJTJCenMwQXNLd3ZvSVpUMGklMkZnJTNEJTNE',
    '_cs_s': '16.0.0.1673434512208',
    '__attentive_pv': '12',
    '__attentive_ss_referrer': 'https://www.clarksusa.com/womens',
    'AKA_A2': 'A',
    'BVBRANDSID': 'c901ca46-f709-45ff-82d2-c9d4212389c4',
    'SameSite': 'None',
    '_uetsid': 'b2d097e0918411ed86a0d1ad99a77c5c',
    '_uetvid': 'b2d0ad30918411ed9fcbc990a8023877'
}

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'https://www.clarksusa.com/womens/all-styles/c/w2?page=5&pageSize=72&productIndex=26161397',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin'
    }

params = {
    'categoryCode': 'w2',
}

def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    try:
        detail_mrp = soup.find('span','product-price-panel__price js-current-price').text
    except:
        detail_mrp = soup.find('span','product-price-panel__price product-price-panel--previous-price js-prev-price').text.strip()
        # detail_mrp = ''
    
    try:
        sale_price2 = soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price').get('content')
    except:
        sale_price2 = ''

    if soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price'):
        saleprice = float(sale_price2)*0.7
    else:
        saleprice = soup.find('span','product-price-panel__price product-price-panel--previous-price js-prev-price').text.strip()

    try:
        listprice = soup.find('span','product-price-panel__price product-price-panel--reduced-price js-current-price').get('content')           
    except:
        listprice = ''
    
    try:
        badge = soup.find('div','product-badge__general').find('img').get('src')
    except:
        badge = ''
    
    try:
        size = soup.find('div','box-selectors__wrapper').find_all('span',{'tabindex':'-1'})

        for i in size:
            IN_STOCK = i.text
    except:
            IN_STOCK = ''
    
    try:
        description = soup.find('div','product-description__text product-description__text--restricted').text
    except:
        description = ''
    product_details = {}
    for i in soup.find_all('div','product-page-tabs__specifications__description-list__row'):
        key = i.find('dt').text
        value = i.find('dd').text
        product_details= {key:value}
    bultheading = [bult.text for bult in soup.find_all('span','product-page-tabs__benefits-text--business-title')]
    bulttext = [ bult.text for bult in  soup.find_all('span','product-page-tabs__benefits-text--business-copy')]
    points = dict(zip(bultheading,bulttext))
    try:
        Comfortable =  points['Comfortable']
    except:
        Comfortable = ''
    
    try:
        Responsible_Leather = points['Responsible \n Leather']
    except:
        Responsible_Leather = ''

    
    images = '||'.join([i.find('img').get('src') for i in soup.find_all('picture')])
    
    data = {
        'detail_mrp':detail_mrp,
        'listprice':listprice,
        'saleprice':saleprice,
        'badge':badge,
        'IN_STOCK':IN_STOCK,
        'description':description,
        'Comfortable':Comfortable,
        'Responsible_Leather':Responsible_Leather,
        'images':images
    }
    data.update(product_details)
    return data

    
alldata = []
def listpage(url):
    url = row['link']
    print(url)
    ctr = url.split('/')[-1]
    params['categoryCode'] = ctr
    response = requests.get('https://www.clarksusa.com/category-search-ajax', params=params, cookies=cookies, headers=headers)
    # print(response,response.url)
    js = response.json()
    # print(js)
    products = js['products']
    for product in products:
        name = product.get('name')
        pro_id = product.get('code')
        pro_URL = 'https://www.clarksusa.com'+product.get('url')
        color = product.get('mediumColor')
        try:
            mrp = product.get('wasPrice').get('formattedValue')
        except:
            mrp = ''
        productBadge = product.get('productBadge') # check which i need ?
        numberOfReviews = product.get('numberOfReviews')
        percentageDiscount =  product.get('percentageDiscount')
        ListPageprice = product.get('price').get('formattedValue')
        image = product.get('imageUrl')
        merchandisingCategory = product.get('merchandisingCategory')
        # variantProductAttributes = product.get('variantProductAttributes')
        # for i in  variantProductAttributes:
        #     color = i.get('colour')
        #     imageUrl = i.get('imageUrl')
        #     productUrl = i.get('productUrl')
        detail = detailpage(pro_URL)

        data = {
            'landingURL':row['link'],
            'name':name,
            'pro_id':pro_id,
            'pro_URL':pro_URL,
            'color':color,
            'mrpList':mrp,
            'productBadge':productBadge,
            'numberOfReviews':numberOfReviews,
            'percentageDiscount':percentageDiscount,
            'ListPageprice':ListPageprice,
            'merchandisingCategory':merchandisingCategory
        }
        alldata.append(data)
        data.update(detail)
        
        print(data)

df = pd.read_excel('SusaUrls.xlsx')
for j in range(len(df)):
# for j in range(1,3):
    row = df.iloc[j].to_dict()
    listpage(row)

# url = 'https://www.clarksusa.com/womens/Womens-Slippers/c/w75'
# url = 'https://www.clarksusa.com/womens/all-styles/c/w2'
# listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('Clarksusa.xlsx', index=False)