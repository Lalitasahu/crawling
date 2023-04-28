from requests import Session
import math
import json
from lxml import html
import pandas as pd
import csv
from bs4 import BeautifulSoup as BS
import re
import requests

s = Session()
# s.headers['user-agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"




cookies = {
    'visid_incap_1686039': 'LGkb3nlNQyuXvCA23j0VTPDcYmMAAAAAQUIPAAAAAABQJyktauI7BDs1wHH7okfH',
    'BVBRANDID': '022332f8-46ab-4852-8363-881284b8f9bb',
    '_gcl_au': '1.1.1502363560.1667423477',
    '_ga_2LJLJKYZ3R': 'GS1.1.1667716052.4.1.1667716125.0.0.0',
    '_ga': 'GA1.2.1653440454.1667423480',
    '_ga_7ZEZ2L98N2': 'GS1.1.1667716051.4.1.1667716119.58.0.0',
    'FPID': 'FPID2.2.0wJ3jCxdfk7N6cvZ9e5twx8NvCyPf9XbM1UqSqADPWw%3D.1667423480',
    '_pin_unauth': 'dWlkPU1qWmtaamd4TTJNdE1XTXdNeTAwWXpWaUxUaGhZVEl0Tm1GbU1EVmtaRGhoTnpaag',
    'IR_PI': 'e5e79c9f-5af2-11ed-8a73-a7ed7598257b%7C1667802519832',
    'inside-au': '1163374577-db0b92e934e4a22127ed0b4eb6002f96d8a4c6531cbc9025ffb6d1bd8f54c9b0-0-0',
    '_hjSessionUser_873034': 'eyJpZCI6ImU1Njc2YTcyLWQ3ZDQtNWEyYy1iM2I5LTk5NzY3NDRmNDM4ZiIsImNyZWF0ZWQiOjE2Njc0MjM0ODI0NDAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gaexp': 'GAX1.2.OaEU5pZLQhGIWE1qu0c46g.19378.0',
    'ASP.NET_SessionId': '2o0hlhtlf15q5jicnpvxa2q4',
    'iSAMS': 'QVbMIQP9o25wreWgzoN7WUkzcDZ/e1zEucdDu4c5xix+9p+c2lsnovhp+ANGyADu8pRqjHnKLpSljn9SKnavqQ==',
    'incap_ses_1132_1686039': '54/UeKQj9D/alM3Zz6y1D89TZ2MAAAAAilrUt4wi0s4Qx6QMNcneKg==',
    'BVBRANDSID': '7dca33d2-0dcb-4db2-a0e4-376a4602c53c',
    'run_fs_for_user': '199',
    'fpGUID': 'ab38714b-c751-49f8-b9eb-57872580eb1d',
    'fpFingerprint': '01665a9f08f77d15a5ed2749d0a88a5a7f70c6a9812af5d33eee28ac0c918d0b',
    'IR_gbd': 'davidjones.com',
    'IR_5504': '1667716119832%7C0%7C1667716119832%7C%7C',
    'FPLC': 'TaIvSHb4E6GrbmGO4pelptKbKKtC8%2BNPbXwMChuDvP%2FOjPQ1SGMCPB7jdb6NhtJFU4mKU1kZQSFL4uosawyeG3TQ1RQNsol%2Bhlo1zI%2BqQ0Qv4%2F8647Ol%2FxWGn830dA%3D%3D',
    'iSAMSShopper': 'N4A0Eo/QjEfwAe7awaBfT+X8ELevA+1j3lCAZiJsunpDOjIQtMvre+qO7mNiRV6wmjJCqZDf1js1gQ8crVdRwA==',
    '_gid': 'GA1.2.1100886179.1667716055',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_873034': 'eyJpZCI6IjRkOTU1MTI5LTc1ZWEtNDc0ZS05MGFhLTUyZTkxZTU2OGFhNCIsImNyZWF0ZWQiOjE2Njc3MTYwNTUzODcsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_uetsid': '1854c6c05d9c11edb1ac7b34062ecfd4',
    '_uetvid': 'e60dc4405af211edb43ed799bf54dde4',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.davidjones.com/men/clothing/pyjamas-and-sleepwear/pyjama-sets',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'visid_incap_1686039=LGkb3nlNQyuXvCA23j0VTPDcYmMAAAAAQUIPAAAAAABQJyktauI7BDs1wHH7okfH; BVBRANDID=022332f8-46ab-4852-8363-881284b8f9bb; _gcl_au=1.1.1502363560.1667423477; _ga_2LJLJKYZ3R=GS1.1.1667716052.4.1.1667716125.0.0.0; _ga=GA1.2.1653440454.1667423480; _ga_7ZEZ2L98N2=GS1.1.1667716051.4.1.1667716119.58.0.0; FPID=FPID2.2.0wJ3jCxdfk7N6cvZ9e5twx8NvCyPf9XbM1UqSqADPWw%3D.1667423480; _pin_unauth=dWlkPU1qWmtaamd4TTJNdE1XTXdNeTAwWXpWaUxUaGhZVEl0Tm1GbU1EVmtaRGhoTnpaag; IR_PI=e5e79c9f-5af2-11ed-8a73-a7ed7598257b%7C1667802519832; inside-au=1163374577-db0b92e934e4a22127ed0b4eb6002f96d8a4c6531cbc9025ffb6d1bd8f54c9b0-0-0; _hjSessionUser_873034=eyJpZCI6ImU1Njc2YTcyLWQ3ZDQtNWEyYy1iM2I5LTk5NzY3NDRmNDM4ZiIsImNyZWF0ZWQiOjE2Njc0MjM0ODI0NDAsImV4aXN0aW5nIjp0cnVlfQ==; _gaexp=GAX1.2.OaEU5pZLQhGIWE1qu0c46g.19378.0; ASP.NET_SessionId=2o0hlhtlf15q5jicnpvxa2q4; iSAMS=QVbMIQP9o25wreWgzoN7WUkzcDZ/e1zEucdDu4c5xix+9p+c2lsnovhp+ANGyADu8pRqjHnKLpSljn9SKnavqQ==; incap_ses_1132_1686039=54/UeKQj9D/alM3Zz6y1D89TZ2MAAAAAilrUt4wi0s4Qx6QMNcneKg==; BVBRANDSID=7dca33d2-0dcb-4db2-a0e4-376a4602c53c; run_fs_for_user=199; fpGUID=ab38714b-c751-49f8-b9eb-57872580eb1d; fpFingerprint=01665a9f08f77d15a5ed2749d0a88a5a7f70c6a9812af5d33eee28ac0c918d0b; IR_gbd=davidjones.com; IR_5504=1667716119832%7C0%7C1667716119832%7C%7C; FPLC=TaIvSHb4E6GrbmGO4pelptKbKKtC8%2BNPbXwMChuDvP%2FOjPQ1SGMCPB7jdb6NhtJFU4mKU1kZQSFL4uosawyeG3TQ1RQNsol%2Bhlo1zI%2BqQ0Qv4%2F8647Ol%2FxWGn830dA%3D%3D; iSAMSShopper=N4A0Eo/QjEfwAe7awaBfT+X8ELevA+1j3lCAZiJsunpDOjIQtMvre+qO7mNiRV6wmjJCqZDf1js1gQ8crVdRwA==; _gid=GA1.2.1100886179.1667716055; _hjIncludedInSessionSample=0; _hjSession_873034=eyJpZCI6IjRkOTU1MTI5LTc1ZWEtNDc0ZS05MGFhLTUyZTkxZTU2OGFhNCIsImNyZWF0ZWQiOjE2Njc3MTYwNTUzODcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _uetsid=1854c6c05d9c11edb1ac7b34062ecfd4; _uetvid=e60dc4405af211edb43ed799bf54dde4',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}



def crawl_detail(url):
    print(url)
    r = requests.get(url,headers=headers,cookies=cookies)

    soup = BS(r.text,'html.parser')
    imgs = "|".join(['https://www.davidjones.com'+i.find('a').get('href') for i in soup.find('ul','alternate-images').find_all('li')])


    try:
        bullets = soup.find('div','long-description').text
    except:
        bullets = ""

    _id = soup.find('div',attrs={'itemscope':'itemscope'}).get('data-product-sku')

    return {
            "_id":_id,
            "imgs":imgs,
            "bullets":bullets
    }

all_data = []


def crawl_list(row):
    url = row['url']
    next_page = url


    while next_page:
        r = requests.get(next_page,headers=headers,cookies=cookies)
        # tree = html.fromstring(r.text)
        soup = BS(r.text,'html.parser')
        # products = tree.xpath('//div[@class="productDescription"]//a/@href')
        products = soup.find('div','products').find_all('h4')
        
        for i in products:
            link = i.find('a').get('href')
            detail = crawl_detail(link)
            data = {
                "_id":detail['_id'],
                "url":link,
                "imgs":detail['imgs'],
                "bullets":detail['bullets'],
                "sub_category":row['Folded_Name'],
                "category":row['Gender_Folder'],
                "cat_url":row['URL']    
                }
            all_data.append(data)
            print(data)
        if soup.find('li','next-prev next'):
            next_page = 'https://www.davidjones.com' + soup.find('li','next-prev next').find('a').get('href')
            print(f'NEXT PAGE.. {next_page}.......................')
        else:
            next_page = False

df = pd.read_excel('input.xlsx')
# for i in range(len(df)):
for i in range(1):
    row = df.iloc[i].to_dict()
    crawl_list(row)

df = pd.DataFrame(all_data)
df.to_excel('davidjones.xlsx',index=False)


