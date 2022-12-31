import requests
import csv
import re
import json
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"


alldata = []
def  reviews(row):
    url = row['pro_Url']
    r = s.get(url)
    print(r.url)
    # product_id = re.search('name": "(.*?)",',r.text).group(1).lower().replace(' ','-') 
    try:
        sku = re.search('sku": "(.*?)"',r.text).group(1).lower()
        product_id = url.split('/')[-1].replace(f'-{sku}','')
    except:
        product_id = url.split('/')[-1]
    # print(product_id)   
    offset = 0
    nextpage = 1
    while nextpage:
        api_url = f'https://api.bazaarvoice.com/data/batch.json?passkey=cad82q4tGUusNItK098edWYOb22bQdujP7McOnf9Bq5o4&apiversion=5.5&displaycode=16784-en_us&resource.q0=reviews&filter.q0=isratingsonly:eq:false&filter.q0=productid:eq:{product_id}&filter.q0=contentlocale:eq:en*,de*,fr,en_US&sort.q0=rating:desc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors,products,comments&filter_reviews.q0=contentlocale:eq:en*,de*,fr,en_US&filter_reviewcomments.q0=contentlocale:eq:en*,de*,fr,en_US&filter_comments.q0=contentlocale:eq:en*,de*,fr,en_US&limit.q0=30&offset.q0={offset}&limit_comments.q0=3&callback=bv_351_25135'
        response = requests.get(
            api_url
            # headers=headers,
        )
        # print(api_url)
        review = json.loads(re.search('bv_351_25135\((.*?)\}\)',response.text).group(1)+'}')
        # offset =  review['BatchedResults']['q0']['Offset']
        TotalResults = review['BatchedResults']['q0']['TotalResults']
        print(offset,TotalResults)
        if offset > TotalResults:
            nextpage = 0
        # print(offset)
        allUsers = review['BatchedResults']['q0']['Results']
        for i in allUsers:
            name = i.get('UserNickname')
            Date = i.get('LastModificationTime')
            title = i.get('Title')
            ReviewText = i.get('ReviewText')
            Shade = i.get('AdditionalFields').get('shade',{}).get('Value')
            Quality_of_Product = i.get('SecondaryRatings',{}).get('Value',{}).get('Value')
            Value_of_Product = i.get('SecondaryRatings',{}).get('Quality',{}).get('Value')
            verifiedPurchaser= i.get('BadgesOrder')
            Photos = i.get('Photos')
            # product_id = i.get('ProductId')
            # reviewAPI = f'https://api.bazaarvoice.com/data/batch.json?passkey=cad82q4tGUusNItK098edWYOb22bQdujP7McOnf9Bq5o4&apiversion=5.5&displaycode=16784-en_us&resource.q0=reviews&filter.q0=isratingsonly:eq:false&filter.q0=productid:eq:{product_id}&filter.q0=contentlocale:eq:en*,de*,fr,en_US&sort.q0=rating:desc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors,products,comments&filter_reviews.q0=contentlocale:eq:en*,de*,fr,en_US&filter_reviewcomments.q0=contentlocale:eq:en*,de*,fr,en_US&filter_comments.q0=contentlocale:eq:en*,de*,fr,en_US&limit.q0=30&offset.q0=8&limit_comments.q0=3&'
            # print(product_id)    

            data = {
                'name':name,
                'product_id':product_id,
                'Data':Date,
                'title':title,
                'ReviewText':ReviewText,
                'Shade':Shade,
                'Quality_of_Product':Quality_of_Product,
                'Value_of_Product':Value_of_Product,
                'verifiedPurchaser':verifiedPurchaser,
                'Photos':Photos

            }

            print(data)
            alldata.append(data)

        if offset == 0:
            offset+=8
        else:
            offset += 30

# url = 'https://kyliecosmetics.com/en-us/kylie-cosmetics/products/batman-collection-mini-eyeliner-set-kc575'
# url = 'https://kyliecosmetics.com/en-us/kylie-cosmetics/products/matte-lip-kit-kc252'



df = pd.read_excel('Kyliecosmetics.xlsx')
for i in range(len(df)):
# for i in range(3):
    row = df.iloc[i].to_dict()
    reviews(row)


df = pd.DataFrame(alldata)
df.to_excel('reviewkylie.xlsx',index=False)


# 