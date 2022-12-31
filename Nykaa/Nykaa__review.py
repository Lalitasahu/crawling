import requests
import re 
import pandas as pd
from lxml import html
from requests import Session
from bs4 import BeautifulSoup as bs
import math
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

cookies = {
    'bcookie': 'f2ce28bb-f405-48d4-bc7b-a69fc0693ee8',
    'EXP_ADP_RV_REORDER': 'A',
    'EXP_ADP_RV_SEGMENT': 'B',
    'EXP_AB_AUTOFILL': 'B',
    'EXP_ADP_RV_VIEW_SIMILAR': 'CONTROL',
    'EXP_AB_PROFILE': 'A',
    'EXP_CART_LOGIN_SEGMENT': 'C',
    'EXP_AB_WISHLIST': 'A',
    'EXP_AB_REVIEW_ALL_IMAGES': 'A',
    'EXP_ADP_RV_HYBRID_PLP': 'CONTROL',
    'EXP_UPDATED_AT': '1671100168311',
    'EXP_SSR_CACHE': '3ae37468b754c37190d7fc436212deec',
    'SITE_VISIT_COUNT': '27',
    'run': '91',
    'D_LST': '1',
    'D_PDP': '1',
    'NYK_PCOUNTER': '3',
    'NYK_ECOUNTER': '3',
    'AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg': '-432600572%7CMCIDTS%7C19354%7CMCMID%7C28620581796132554052222047729281922179%7CMCAAMLH-1672792387%7C12%7CMCAAMB-1672792387%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1672194787s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2',
    's_nr365': '1672188361690-Repeat',
    'd_info': '1536_864',
    'PHPSESSID': 'ob94g9nmj7r886v7lp638hdp26',
    'head_data_react': '{"id":"","nykaa_pro":false,"group_id":""}',
    'pro': 'false',
    '_gcl_au': '1.1.1900515629.1672123077',
    '_ga_LKNEBVRZRG': 'GS1.1.1672187447.5.1.1672188479.60.0.0',
    '_ga': 'GA1.2.1582030568.1672123077',
    'mfKey': 'tcm0ij.1672123077071',
    '_gid': 'GA1.2.1686808399.1672123078',
    'deduplication_cookie': 'GooglePaid',
    'deduplication_cookie': 'GooglePaid',
    'mf_visitid': 'ioj00x.1672188362227',
    'mf_utms': '%7B%22skuId%22%3A%221171878%22%2C%22ptype%22%3A%22reviews%22%7D',
    '__cfruid': 'da5df5a05b79404aab064aff0d21edf97e65dca7-1672136049',
    'utm_source': 'googlepaid',
    'utm_medium': 'pla',
    'utm_campaign': '',
    'AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg': '1',
    's_cc': 'true',
    '_gcl_aw': 'GCL.1672135906.CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE',
    '_ttgclid': 'CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE',
    '_ttgclid': 'CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE',
    '_ttgclid': 'CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE',
    '_gac_UA-31866293-9': '1.1672135907.CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE',
    'cto_bundle': '0iLvj19HN3phVTRpU3FXZFg1eXNQelUlMkJxbjllTjg0ekR2NTFYQXZTQVhibU8zWkpzcXhTY1JBOFRnbFpWa1Q5TWZNNk9ucDh5Q3BYTnJiMzBodmI0bVZxM08lMkJ1b2NPeTF2JTJCaDh1ajcxNEZSYnZPazJsdGpCQlNpQktSWWYlMkJrbjdGcXZvdmJBWG9mVE5iOW1qWXJKVXc0djRUZyUzRCUzRA',
    's_sq': '%5B%5BB%5D%5D',
    '__cf_bm': 'l9qD6mmDRSbpwJERxqWRjT8PnQj4X8DGTLCZ2VFQmhc-1672188627-0-AY4ABIegfhMWUbb6Qj3Q7eELhT6aocj2eBVS6YvEeIznRwKWYz3O8TPM3MLw2xPUGkjnBQyXBZMH9GxQobXLWNg=',
    'NYK_VISIT': 'f2ce28bb-f405-48d4-bc7b-a69fc0693ee8~1672187446716',
    'countryCode': 'IN',
    'storeId': 'nykaa',
    'lux_uid': '167218758621983992',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.nykaa.com/cetaphil-bhr-brightening-night-comfort-cream/reviews/1171878?skuId=1171878&ptype=reviews',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'bcookie=f2ce28bb-f405-48d4-bc7b-a69fc0693ee8; EXP_ADP_RV_REORDER=A; EXP_ADP_RV_SEGMENT=B; EXP_AB_AUTOFILL=B; EXP_ADP_RV_VIEW_SIMILAR=CONTROL; EXP_AB_PROFILE=A; EXP_CART_LOGIN_SEGMENT=C; EXP_AB_WISHLIST=A; EXP_AB_REVIEW_ALL_IMAGES=A; EXP_ADP_RV_HYBRID_PLP=CONTROL; EXP_UPDATED_AT=1671100168311; EXP_SSR_CACHE=3ae37468b754c37190d7fc436212deec; SITE_VISIT_COUNT=27; run=91; D_LST=1; D_PDP=1; NYK_PCOUNTER=3; NYK_ECOUNTER=3; AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg=-432600572%7CMCIDTS%7C19354%7CMCMID%7C28620581796132554052222047729281922179%7CMCAAMLH-1672792387%7C12%7CMCAAMB-1672792387%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1672194787s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2; s_nr365=1672188361690-Repeat; d_info=1536_864; PHPSESSID=ob94g9nmj7r886v7lp638hdp26; head_data_react={"id":"","nykaa_pro":false,"group_id":""}; pro=false; _gcl_au=1.1.1900515629.1672123077; _ga_LKNEBVRZRG=GS1.1.1672187447.5.1.1672188479.60.0.0; _ga=GA1.2.1582030568.1672123077; mfKey=tcm0ij.1672123077071; _gid=GA1.2.1686808399.1672123078; deduplication_cookie=GooglePaid; deduplication_cookie=GooglePaid; mf_visitid=ioj00x.1672188362227; mf_utms=%7B%22skuId%22%3A%221171878%22%2C%22ptype%22%3A%22reviews%22%7D; __cfruid=da5df5a05b79404aab064aff0d21edf97e65dca7-1672136049; utm_source=googlepaid; utm_medium=pla; utm_campaign=; AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg=1; s_cc=true; _gcl_aw=GCL.1672135906.CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE; _ttgclid=CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE; _ttgclid=CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE; _ttgclid=CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE; _gac_UA-31866293-9=1.1672135907.CjwKCAiAzKqdBhAnEiwAePEjksMPEflm6ympm8jU7blHcjHS1ty_7LZmXHmbgfw9JnibvKG88qdYzBoCUkcQAvD_BwE; cto_bundle=0iLvj19HN3phVTRpU3FXZFg1eXNQelUlMkJxbjllTjg0ekR2NTFYQXZTQVhibU8zWkpzcXhTY1JBOFRnbFpWa1Q5TWZNNk9ucDh5Q3BYTnJiMzBodmI0bVZxM08lMkJ1b2NPeTF2JTJCaDh1ajcxNEZSYnZPazJsdGpCQlNpQktSWWYlMkJrbjdGcXZvdmJBWG9mVE5iOW1qWXJKVXc0djRUZyUzRCUzRA; s_sq=%5B%5BB%5D%5D; __cf_bm=l9qD6mmDRSbpwJERxqWRjT8PnQj4X8DGTLCZ2VFQmhc-1672188627-0-AY4ABIegfhMWUbb6Qj3Q7eELhT6aocj2eBVS6YvEeIznRwKWYz3O8TPM3MLw2xPUGkjnBQyXBZMH9GxQobXLWNg=; NYK_VISIT=f2ce28bb-f405-48d4-bc7b-a69fc0693ee8~1672187446716; countryCode=IN; storeId=nykaa; lux_uid=167218758621983992',
    'If-Modified-Since': 'Wed, 28 Dec 2022 00:48:49 GMT',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'pageNo': '2',
    'filters': 'DEFAULT',
    'domain': 'nykaa',
}

allreviews = []
def review(url):
    r = s.get(url)
    tree = html.fromstring(r.text)
    reviews = tree.xpath('//div[@class="css-1hvvm95"]//text()')[-2]
    pages = math.ceil(int(reviews)/20)
    nextPage = True
    num = 1 
    while nextPage:
    # print(pages)
    # for i in range(1,pages+1):
        params['pageNo'] = str(num)
        response = requests.get(
        'https://www.nykaa.com/gateway-api/products/1171878/reviews',
        params=params,
        cookies=cookies,
        headers=headers,
        )
        # print(response.url)
        js = response.json()
        print(js)
        if js['response']['page'] <= pages:
            num += 1
            nextPage = True
        else:
            nextPage = False

        # print(js)
        reviews = js['response']['reviewData']
        for i in reviews:
            name = i.get('name')
            id = i.get('id')
            childId = i.get('childId')
            title = i.get('title')
            description = i.get('description')
            Date = i.get('reviewCreationText')
            likeCount = i.get('likeCount')   
            rating = i.get('rating')
            images = ''.join(i.get('images'))
            userImageCount = i.get('userImageCount')
            userReviewCount = i.get('userReviewCount')
            label = i.get('label')

            data = {
                'pro_url':response.url,
                'Name':name,
                'id':id,
                'chilId':childId,
                'title':title,
                'description':description,
                'Date':Date,
                'likeCount':likeCount,
                'rating':rating,
                'images':images,
                'ImageCount':userImageCount,
                'userReviewCount':userReviewCount,
                'label':label,
                
            } 

            allreviews.append(data)
            print(data)


url = 'https://www.nykaa.com/cetaphil-bhr-brightening-night-comfort-cream/p/1171878'
# url = 'https://www.nykaa.com/de-fabulous-reviver-hair-repair-conditioner-250ml/p/18413'
review(url)
df = pd.DataFrame(allreviews)
df.to_excel('review1.xlsx',index=False)