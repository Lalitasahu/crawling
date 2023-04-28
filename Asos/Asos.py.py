import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
cookies = {
    '_abck': 'F64BDC82F287EDDC69DE5989AAACF2EA~0~YAAQvW0/FxIEpT2EAQAAT0TSYAhTWVO1vIoO+TM9g4mmGo+VfXU1Obv291TnxBOTaVG965Ug3NdVs9m9UJPVNzYcDyF1aWUk6N4qZCWwJ8ADV9EBwtJwU9RnIrb28r1KACvcD6J2ek34h7gnAu8slaWrB+tHMAfg2wKTznjXeM1TdwwzHhLKl7nXYZjIDsZwUruQQuHe3+8oAxp2a7EDgbes+RvEFUVSU/FFuGJKaboJIxLjIGQ3hZuzvMxlyYH7P8ARjOSJLL8X28FIbNYMYQLQr2fn2s4mPBYm1fwGTdzUVakzRmtjMaOurNoRLxua+psP5LJeHFRANT4d4XGyRqetbegkwbY5pjVKIunw07hkVcxOS4cseHujCsB/+JJZqtTe+QRZ8maBif4g7gpDlgiCAAmjbaM=~-1~||1-OaGiRTpRQH-1-10-1000-2||~1668075185',
    'bm_sz': 'A2C2836182A7339E089EC10BCB1C4B30~YAAQjwVaaN/SalKEAQAAXL2sYBHb8hXG1BE8Hv8MRdFVJ2GXIlkDaW94j31Hc/ioCFe+ibTIAPZ/Nuimif+oDXADGeTuaPGwqZUFi/UbpzUbc7znJ9qyxk2DAJG/2K4O0RCjTeFqx6gNDvw+5BQ2Zo5K2vqBSaIX8ppD9Z+nvTSfGHZnlhVhuVfTpPF0PrrasOhdrQ4OmfBF1v6vgKcV+eZjgr7Tqx6l06G9ipcpuZE4iwMK/QzHoqF3zbKDgOvzBPtULid2Ce6L3XEij1eL6WGf1cZXLz4G2ZCHbXlwXfcU~3359286~3621188',
    'AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg': '-1303530583%7CMCMID%7C13674605133331995881798224071525364016%7CMCAID%7CNONE%7CMCOPTOUT-1668076458s%7CNONE%7CMCAAMLH-1668674058%7C12%7CMCAAMB-1668674058%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C3.3.0%7CMCCIDH%7C0%7CMCSYNCSOP%7C411-19314',
    's_pers': '%20s_vnum%3D1669833000640%2526vn%253D1%7C1669833000640%3B%20eVar225%3D24%7C1668073447016%3B%20visitCount%3D1%7C1668073447017%3B%20gpv_e231%3Db924a4a1-7f87-4854-920d-5e3442ca1ed1%7C1668073447881%3B%20s_invisit%3Dtrue%7C1668073447882%3B%20s_nr%3D1668071647882-New%7C1699607647882%3B%20gpv_e47%3Dno%2520value%7C1668073447883%3B%20gpv_p10%3Ddesktop%2520us%257Ccategory%2520page%257C10117%2520page%25201%2520refined%7C1668073447883%3B',
    'siteChromeVersion': 'au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12',
    'keyStoreDataversion': 'dup0qtf-35',
    'asosAffiliate': 'affiliateId=17295',
    'browseCountry': 'US',
    'asos': 'PreferredSite=&currencyid=2&currencylabel=USD&customerguid=48c5da5d3a5d43d480f015aa2dd0ae15&topcatid=1000',
    'browseCurrency': 'USD',
    'browseLanguage': 'en-US',
    'browseSizeSchema': 'US',
    'storeCode': 'US',
    'currency': '2',
    'stc-welcome-message': 'cappedPageCount=2&resolvedDeliveryCountry=IN&userTookActionOnWelcomeMessage=true',
    'featuresId': '315863ce-f2aa-4216-aeb8-9b698e6acee4',
    'ak_bmsc': '9B104923D5F5A0C1C47B5CC2ADAC612C~000000000000000000000000000000~YAAQ3O/IF+DJL1KEAQAAWIuvYBHgconiU9O8N03gbXYeUqPxOnmKgMwA/wEZq/DLBIGMIbNXNEctfHjzBtKIUJ1we42Herv5iCmW9F+0G8223AUbhg8aXFO2qGxJVjNL5qimJUA5M6xxbGGhHW7vX/akaAbBH+RkaiB+Odmu2nebveo520+F+E0lBMjvY+DNwgpLS+6FM+5uS3xICefs3OshGUKO4rJB/8+B0ZR2q3EXi455AedVQriekFfMcY9ajvjo0RL6bQHGC0K4KfRHaqbtZa02FoXXVHRmFrKOdO0cTHpLtpW4ttU0sH9vv+YHo4lNx/8053q5pQTW+9YV/D4hy13Am1p0EtkQc3UFBGfgFm2SpmjKch7K/Tj4acjilrSUcmtyYTW68l7eICqhKC0840xdQdY7aelqWl2cYEnGpb4CyIrrnEOoTldKZAHK/93ovMdw4kpkHP2UWagl6GVs9zcfQ8fqwkYpd1BQIlO7piUzeBigWgZz/Eh+JDjspFw92Xq1gB2SLL4gBAjCVICH/KahjyvAKoXNBbA=',
    'asos-b-sdv629': 'dup0qtf-35',
    'RT': '"z=1&dm=asos.com&si=4b9c473f-c314-4130-afd2-a9c4416cf53a&ss=laatbkjb&sl=o&tt=11o9&bcn=%2F%2F684d0d4c.akstat.io%2F&ld=1gyrd&nu=flfui3m0&cl=1htpk"',
    's_ecid': 'MCMID%7C13674605133331995881798224071525364016',
    'asos-perx': '48c5da5d3a5d43d480f015aa2dd0ae15||19020b5daca84f86b1ba1189a59c49e9',
    '_s_fpv': 'true',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Nov+10+2022+14%3A44%3A08+GMT%2B0530+(India+Standard+Time)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    '_gcl_au': '1.1.1821067939.1668069184',
    'bt_stdstatus': 'NOTSTUDENT',
    '_cs_c': '0',
    '_cs_id': '0ce48aa1-0b66-a81a-e50c-6505c82d85b9.1668069184.1.1668071648.1668069184.1628755191.1702233184060',
    '_cs_s': '14.0.0.1668073448824',
    '_ga_1JR0QCFRSY': 'GS1.1.1668069184.1.1.1668071670.25.0.0',
    '_ga': 'GA1.2.464033323.1668069184',
    'FPLC': 'g4hCq9RkwF20KyyCN6G48%2BhRSVrA2uTYrgWwNChCyxs%2Bd2ClaOgiKmB%2Fc5ObgVUiK5bISg0wQpjMDn0UbLNKy8n9rEX0cl0SUp7lXlcBUWIOmtXMz0%2BtSpPpWf86%2Bg%3D%3D',
    'FPID': 'FPID2.2.nvKbME3Qn2mdIRFWuWX8Lfxm7j4iA2NgZPMq2C58Dvk%3D.1668069184',
    'FPAU': '1.1.1821067939.1668069184',
    'floor': '1000',
    'bm_mi': 'FC0E95426F3010EEB187CDAB06A93B7F~YAAQ3O/IF77CL1KEAQAA1gavYBFOQ8Cf/aoSImYlDhxIzlPMbQEy5CryJKD7qrbQm4EjsgpgpepN/d1edmxFM2DfTq0F9IotKe2ViE5JLk5L4D1lssorriCDz726Gl0RMmXqVVXs7PlMZ9k4arxff9b6RZFdmkCT6jCEukVIxwiZdraG4ajw02kfST3m7o/HypeUeIL/vm++jTeIM1ymdd6zYT9ixqM4XVB45laHIer5+NaehNRLcWYpDwH0wa++amOgn2RstajZqigTjxa3HyqMxapFdvKvHGnj4rbZVPgdBwnEGl4L82iAFmv+cwC+4Ew/QQ4udX4dGH9GWjEIARf8Y3Gc9w==~1',
    '_gid': 'GA1.2.42942709.1668069188',
    'geocountry': 'IN',
    'plp_columsCount': 'fourColumns',
    'AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg': '1',
    's_cc': 'true',
    's_sq': 'asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520us%25257Ccategory%252520page%25257C10117%252520page%2525201%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
    '__gads': 'ID=ebb344c45200adc4-22f0980945d800fc:T=1668069380:S=ALNI_MYsA-5u_piCpyirG9BNJyCQKmUNJA',
    '__gpi': 'UID=00000b79172253a5:T=1668069380:RT=1668069380:S=ALNI_MY-QoPGkwUj8HoGu_b8rzMjQpaijw',
    '_cs_mk_aa': '0.23744449304794646_1668071639437',
    '_dc_gtm_UA-1005942-121': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'asos-cid': 'ad488488-66b9-478f-8bc4-8bf60db8a354',
    'asos-c-plat': 'web',
    'asos-c-name': '@asosteam/asos-web-product-listing-page',
    'asos-c-ver': '1.2.0-0702cbca30a6-7379',
    'Connection': 'keep-alive',
    'Referer': 'https://www.asos.com/us/women/swimwear-beachwear/bikinis/cat/?cid=10117&ctaref=cat_header&page=2',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_abck=F64BDC82F287EDDC69DE5989AAACF2EA~0~YAAQvW0/FxIEpT2EAQAAT0TSYAhTWVO1vIoO+TM9g4mmGo+VfXU1Obv291TnxBOTaVG965Ug3NdVs9m9UJPVNzYcDyF1aWUk6N4qZCWwJ8ADV9EBwtJwU9RnIrb28r1KACvcD6J2ek34h7gnAu8slaWrB+tHMAfg2wKTznjXeM1TdwwzHhLKl7nXYZjIDsZwUruQQuHe3+8oAxp2a7EDgbes+RvEFUVSU/FFuGJKaboJIxLjIGQ3hZuzvMxlyYH7P8ARjOSJLL8X28FIbNYMYQLQr2fn2s4mPBYm1fwGTdzUVakzRmtjMaOurNoRLxua+psP5LJeHFRANT4d4XGyRqetbegkwbY5pjVKIunw07hkVcxOS4cseHujCsB/+JJZqtTe+QRZ8maBif4g7gpDlgiCAAmjbaM=~-1~||1-OaGiRTpRQH-1-10-1000-2||~1668075185; bm_sz=A2C2836182A7339E089EC10BCB1C4B30~YAAQjwVaaN/SalKEAQAAXL2sYBHb8hXG1BE8Hv8MRdFVJ2GXIlkDaW94j31Hc/ioCFe+ibTIAPZ/Nuimif+oDXADGeTuaPGwqZUFi/UbpzUbc7znJ9qyxk2DAJG/2K4O0RCjTeFqx6gNDvw+5BQ2Zo5K2vqBSaIX8ppD9Z+nvTSfGHZnlhVhuVfTpPF0PrrasOhdrQ4OmfBF1v6vgKcV+eZjgr7Tqx6l06G9ipcpuZE4iwMK/QzHoqF3zbKDgOvzBPtULid2Ce6L3XEij1eL6WGf1cZXLz4G2ZCHbXlwXfcU~3359286~3621188; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C13674605133331995881798224071525364016%7CMCAID%7CNONE%7CMCOPTOUT-1668076458s%7CNONE%7CMCAAMLH-1668674058%7C12%7CMCAAMB-1668674058%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C3.3.0%7CMCCIDH%7C0%7CMCSYNCSOP%7C411-19314; s_pers=%20s_vnum%3D1669833000640%2526vn%253D1%7C1669833000640%3B%20eVar225%3D24%7C1668073447016%3B%20visitCount%3D1%7C1668073447017%3B%20gpv_e231%3Db924a4a1-7f87-4854-920d-5e3442ca1ed1%7C1668073447881%3B%20s_invisit%3Dtrue%7C1668073447882%3B%20s_nr%3D1668071647882-New%7C1699607647882%3B%20gpv_e47%3Dno%2520value%7C1668073447883%3B%20gpv_p10%3Ddesktop%2520us%257Ccategory%2520page%257C10117%2520page%25201%2520refined%7C1668073447883%3B; siteChromeVersion=au=12&com=12&de=12&dk=12&es=12&fr=12&it=12&nl=12&pl=12&roe=12&row=12&ru=12&se=12&us=12; keyStoreDataversion=dup0qtf-35; asosAffiliate=affiliateId=17295; browseCountry=US; asos=PreferredSite=&currencyid=2&currencylabel=USD&customerguid=48c5da5d3a5d43d480f015aa2dd0ae15&topcatid=1000; browseCurrency=USD; browseLanguage=en-US; browseSizeSchema=US; storeCode=US; currency=2; stc-welcome-message=cappedPageCount=2&resolvedDeliveryCountry=IN&userTookActionOnWelcomeMessage=true; featuresId=315863ce-f2aa-4216-aeb8-9b698e6acee4; ak_bmsc=9B104923D5F5A0C1C47B5CC2ADAC612C~000000000000000000000000000000~YAAQ3O/IF+DJL1KEAQAAWIuvYBHgconiU9O8N03gbXYeUqPxOnmKgMwA/wEZq/DLBIGMIbNXNEctfHjzBtKIUJ1we42Herv5iCmW9F+0G8223AUbhg8aXFO2qGxJVjNL5qimJUA5M6xxbGGhHW7vX/akaAbBH+RkaiB+Odmu2nebveo520+F+E0lBMjvY+DNwgpLS+6FM+5uS3xICefs3OshGUKO4rJB/8+B0ZR2q3EXi455AedVQriekFfMcY9ajvjo0RL6bQHGC0K4KfRHaqbtZa02FoXXVHRmFrKOdO0cTHpLtpW4ttU0sH9vv+YHo4lNx/8053q5pQTW+9YV/D4hy13Am1p0EtkQc3UFBGfgFm2SpmjKch7K/Tj4acjilrSUcmtyYTW68l7eICqhKC0840xdQdY7aelqWl2cYEnGpb4CyIrrnEOoTldKZAHK/93ovMdw4kpkHP2UWagl6GVs9zcfQ8fqwkYpd1BQIlO7piUzeBigWgZz/Eh+JDjspFw92Xq1gB2SLL4gBAjCVICH/KahjyvAKoXNBbA=; asos-b-sdv629=dup0qtf-35; RT="z=1&dm=asos.com&si=4b9c473f-c314-4130-afd2-a9c4416cf53a&ss=laatbkjb&sl=o&tt=11o9&bcn=%2F%2F684d0d4c.akstat.io%2F&ld=1gyrd&nu=flfui3m0&cl=1htpk"; s_ecid=MCMID%7C13674605133331995881798224071525364016; asos-perx=48c5da5d3a5d43d480f015aa2dd0ae15||19020b5daca84f86b1ba1189a59c49e9; _s_fpv=true; OptanonConsent=isIABGlobal=false&datestamp=Thu+Nov+10+2022+14%3A44%3A08+GMT%2B0530+(India+Standard+Time)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_au=1.1.1821067939.1668069184; bt_stdstatus=NOTSTUDENT; _cs_c=0; _cs_id=0ce48aa1-0b66-a81a-e50c-6505c82d85b9.1668069184.1.1668071648.1668069184.1628755191.1702233184060; _cs_s=14.0.0.1668073448824; _ga_1JR0QCFRSY=GS1.1.1668069184.1.1.1668071670.25.0.0; _ga=GA1.2.464033323.1668069184; FPLC=g4hCq9RkwF20KyyCN6G48%2BhRSVrA2uTYrgWwNChCyxs%2Bd2ClaOgiKmB%2Fc5ObgVUiK5bISg0wQpjMDn0UbLNKy8n9rEX0cl0SUp7lXlcBUWIOmtXMz0%2BtSpPpWf86%2Bg%3D%3D; FPID=FPID2.2.nvKbME3Qn2mdIRFWuWX8Lfxm7j4iA2NgZPMq2C58Dvk%3D.1668069184; FPAU=1.1.1821067939.1668069184; floor=1000; bm_mi=FC0E95426F3010EEB187CDAB06A93B7F~YAAQ3O/IF77CL1KEAQAA1gavYBFOQ8Cf/aoSImYlDhxIzlPMbQEy5CryJKD7qrbQm4EjsgpgpepN/d1edmxFM2DfTq0F9IotKe2ViE5JLk5L4D1lssorriCDz726Gl0RMmXqVVXs7PlMZ9k4arxff9b6RZFdmkCT6jCEukVIxwiZdraG4ajw02kfST3m7o/HypeUeIL/vm++jTeIM1ymdd6zYT9ixqM4XVB45laHIer5+NaehNRLcWYpDwH0wa++amOgn2RstajZqigTjxa3HyqMxapFdvKvHGnj4rbZVPgdBwnEGl4L82iAFmv+cwC+4Ew/QQ4udX4dGH9GWjEIARf8Y3Gc9w==~1; _gid=GA1.2.42942709.1668069188; geocountry=IN; plp_columsCount=fourColumns; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520us%25257Ccategory%252520page%25257C10117%252520page%2525201%252520refined%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; __gads=ID=ebb344c45200adc4-22f0980945d800fc:T=1668069380:S=ALNI_MYsA-5u_piCpyirG9BNJyCQKmUNJA; __gpi=UID=00000b79172253a5:T=1668069380:RT=1668069380:S=ALNI_MY-QoPGkwUj8HoGu_b8rzMjQpaijw; _cs_mk_aa=0.23744449304794646_1668071639437; _dc_gtm_UA-1005942-121=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'channel': 'desktop-web',
    'country': 'US',
    'currency': 'USD',
    'keyStoreDataversion': 'dup0qtf-35',
    'lang': 'en-US',
    'limit': '72',
    'offset': '72',
    'rowlength': '4',
    'store': 'US',
    'tst-search-sponsored-products': 'true',
}


def crawl_detail(url):
    print(url)
    r=s.get(url,headers=headers,cookies=cookies)
    
    soup=bs(r.text,'html.parser')
    # print(soup.prettify())
    id=soup.find('div','product-code').find('p').text
    images='||'.join([image.find('img').get('src') for image in soup.find_all('li','image-thumbnail')])
    discription=soup.find('div','product-description').text.replace('\n','')
    print(id)
    return {
        'id':id,
        'images':images,
        'discription':discription
    }

all_data=[]

def crawl_list(row):
    
        response = requests.get('https://www.asos.com/api/product/search/v2/categories/10117', params=params, cookies=cookies, headers=headers)
        # print(response.url)
        js=response.json()
        # print(js)
        products=js['products']
        # print(products)ip
        for i in products:
            pro_url='https://www.asos.com/us/asos-design/'+i.get('url')
            # print(pro_url)
            try:            
                detail=crawl_detail(pro_url)
                data={'pro_url':pro_url,
                'id':detail['id'],
                'images':detail['images'],
                'discription':detail['discription'],
                #    "sub_category":row['Folded_Name'],
                #     "category":row['Gender_Folder'],
                #    "cat_url":row['url'] 
                    }
                all_data.append(data)
                print(all_data)
            except:
                pass



df = pd.read_excel('input.xlsx')
# for i in range(len(df)):
for i in range(1,2):
    row = df.iloc[i].to_dict()
    crawl_list(row)

df = pd.DataFrame(all_data)
df.to_excel('Cupshe.xlsx',index=False)
