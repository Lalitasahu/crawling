import re
import os
import json
import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
import concurrent.futures
s = Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.lenovo.com/gb/en/search?text=laptop&fsid=1',
    'Connection': 'keep-alive',
    # 'Cookie': f'_abck=38FFA3FD8B7C4AE2FD3DB8008412743E~0~YAAQtl06F1yxcxeFAQAA7puFGgn27YpLagPCP5xES/AyRA45vC3usmeH8bsxnqaEY9ZWxGAOzjyI6nmp44LvqW76VVdXGMaN2mS0v3YOazvRcNQ0Yh1BrBJ3+Xebjhf8aSoHjj73UVdwVuZH54zoixw9Zmx0sWMVWEWwHGlpFX7dgRrK8AuGEPNEfVPsDzdzmS3MSe9hzXAxl/yk7LV45MdMXrtjgvJPaCjrE3HmGZHqHOjjC6276G/G55KEn2oRpgdPzxhKy/5XGCvndTfiof0Wz+AoXSfHYXo/nbaPqGNfiHpNJ3R8MwfmrZwFjsiknocOVNnSA0uNolDBy7pCcOujnEkRMiBxhH925r2KFAEBlIOMpHJ/CWFZ+iUSgVYet3DDWMAgwrIkMoUSV/PLBHxlu4CNiv6Zpw==~-1~-1~1671190729; split=test; split10=control; utag_main=v_id:0183b77f38160034ee27834da85405050008500d00978{_sn:2$_se:1$_ss:1$_st:1671188918416$_ga:0183b77f38160034ee27834da85405050008500d00978$dc_visit:2$ses_id:1671187118416%3Bexp-session$_pn:1%3Bexp-session$criteo_sync:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:ap-east-1%3Bexp-session;} kndctr_F6171253512D2B8C0A490D45_AdobeOrg_identity=CiY2NjUxODQ4NzU3NjE0OTE5NTk0MDI1NDUyMTY1NTMxNDQzNjU5N1IRCNPH%5Fbu7MBABGAEqBElORDGgAZf7qo7RMKgBtarVzKvs8Z0T8AGOuZbU0TA%3D; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=MCMID|66518487576149195940254521655314436597; BVBRANDID=431bcd48-5c26-4b0d-a434-c7c5d1240eac; hero-session-23ba646a-b0d7-46ca-af03-cc5bf3b24d83=author=client&expires=1702723118542&visitor=7fffd157-5c93-4fc6-888c-3c772b76315c; s_tslv=1671187115967; s_vnc365=1702723115968%26vn%3D6; _ga_LXNLK45HZF=GS1.1.1671187116.6.0.1671187129.0.0.0; _ga=GA1.1.701193512.1665230916; inside-eu2=505712570-46f4011a36c4747c127723f3754c6fe6808faf042444be68a365e413af25aebe-0-0; _evidon_consent_cookie={"consent_date":"2022-10-08T12:08:36.289Z","categories":{"6":true},"vendors":{"6":{"11":true,"38":true,"51":true,"66":true,"80":true,"81":true,"103":true,"108":true,"242":true,"257":true,"307":true,"321":true,"342":true,"355":true,"384":true,"395":true,"414":true,"467":true,"480":true,"503":true,"608":true,"641":true,"642":true,"662":true,"828":true,"831":true,"933":true,"1028":true,"1061":true,"1272":true,"1552":true,"1727":true,"2191":true,"2253":true,"2450":true,"2468":true,"2516":true,"2594":true,"2708":true,"2937":true,"3042":true,"3058":true,"3490":true,"3778":true,"3857":true,"4526":true,"4748":true,"4941":true,"5296":true,"5385":true,"5678":true,"6359":true,"6531":true,"6609":true,"6638":true,"6723":true}},"cookies":{"6":true},"consent_type":1}; _ga_VBYSKTNF8V=GS1.1.1671187116.2.0.1671187129.0.0.0; _ga_K1R42ZM57S=GS1.1.1671187116.2.0.1671187129.0.0.0; _ga_XKJTHS007F=GS1.1.1671187116.2.0.1671187129.0.0.0; _gcl_au=1.1.1076096183.1665230917; _mibhv=anon-1665230917695-1734072972_8719; _tt_enable_cookie=1; _ttp=a7b0cda7-9087-405a-9895-3f63af64d54c; _mkto_trk=id:183-WCT-620&token:_mch-lenovo.com-1665230920111-34832; QuantumMetricUserID=74fbff938cad683a35a8b41e79875333; knexus_d13d58c021c52c7f020be3660bbea05b===QNxAjM3ETN3gzX452a; knexus_8a732e0ed93a959059be7e5cb2803679===QfiEDM4UjM5AzMyUjN2ETNxAjM3ETN3gzX452afRWazJiOi42bpN3clN3X0NXYsJCLiEDM4UjM5AzMyUjN2ETNxAjM3ETN3gzX452afRWazJiOi42bpN3clN3X05WZyJXdjJye; leid=1.huRjbCa2ec8; inside-us3=108873466-29014a8969c2e9106c9413f8b391b1ca49d05371015e34a2de5b7a4858008c78-0-0; _fbp=fb.1.1667666664753.798012961; IR_PI=3e0f36fb-5d29-11ed-8a73-a7ed7598257b%7C1667758131679; _rdt_uuid=1667666665904.7599b6e3-a726-4719-a1fb-473a30f64a40; _ga_1RPSEV71KD=GS1.1.1667671729.2.1.1667672629.60.0.0; _ga_X0H82YEL7G=GS1.1.1667671729.2.1.1667672629.60.0.0; ki_t=1667666666745%3B1667666666745%3B1667671732534%3B1%3B5; ki_r=; _uetvid=1b3218305d2911ed9e5359d95ef42fa7; mp_lenovo_us_mixpanel=%7B%22distinct_id%22%3A%20%2218448ade2a2371-022a22dd93a7038-c535426-144000-18448ade2a378d%22%2C%22bc_persist_updated%22%3A%201667666666148%7D; fusionQueryId=HdQ4ts2rod; fusionEXPID=flash_anz_app_qpl_dir_G2FHybris; aamtest1=seg=abc%2Cseg=def%2Cseg=ghi; _ga_LNFXZCR83J=GS1.1.1671094207.2.0.1671094214.0.0.0; _ga_S747NZ5XE2=GS1.1.1671094207.2.0.1671094214.0.0.0; _ga_740XK5GERP=GS1.1.1671094207.2.0.1671094215.0.0.0; RT="z=1&dm=lenovo.com&si=707d33e0-dc6a-4cef-b077-88a54ed33810&ss=lbqdnnzx&sl=1&tt=4q3&bcn=%2F%2F684d0d4b.akstat.io%2F&ld=4sz"; ftv_for_auen=%252Fpc%252F; inside-au=1180815480-383f2076c0fd5a57430a843fe082cd7db9a1c89e934dcf721fea43b4d43939f8-0-0; cto_bundle=xL911193dkRKeWwlMkZwSUtSSWIwNGF6elhDWkU5M2E2a1BKWHVqY3olMkJtZEZZbEY4OXZoMCUyQk9wZ1E3UmJDJTJGQ2tValhQbVdScEpGSlRXQ3p1bnVvVk5YJTJGbFBuMDQ2QkQ4am9TSEZaTEFIWFJOQ3lSSFhJZXpLdVZKdUlzTWhuMzdWeGU4eUh2N1NEMWlSVndFZ0FTYVJQWkJ4SFl3JTNEJTNE; mp_lenovo_au_mixpanel=%7B%22distinct_id%22%3A%20%2218448ade2a2371-022a22dd93a7038-c535426-144000-18448ade2a378d%22%2C%22bc_persist_updated%22%3A%201671040656780%7D; AKA_A2=A; akavpau_WaitingRoomController=1671187542~id=65885d16b9beb23bd4bd96470924243b; ak_bmsc=C6BF4503362F32E7BB1EC29D1140B87C~000000000000000000000000000000~YAAQtl06F6uxcxeFAQAATZ6FGhL5AiW6loEBX+0G37PjBo1S2kLF/8hOqK6EUzAPBy7p5gcbl4VB5QAj657FPMFJXVWsKsjeSp4Hw658OZMr+EuTkBqWn9Ps6bOOjv5HfU//PW9dNV6GrgGHEtpGNsEQw8lAOjiEuAg4QqpJrXvH/aWXQ/46jntRfgoZYePdT/Qnaw6UxpXjmk0cVkAHDEQBiZOiAaFjEMMkm/MgUFvYBu/6g7ZOvLeFzrsYJgck1oaHD7R18oysCPRITnUG7/UfBOCCUMBUb/17p0mYF4GAmafL+HKayR7+g2WT1vLMk52psHGV1xfJA88PN6RRxDfgdWAciH0nbtLRkE3cUjugrQ7ByrcqZtTRjV9cQFksidtuTVrXUCMQ9+HMoKwyP+YRr7P1nZdp9N8LSSat5zoo6TRhGjy2t9tlfFaTdIcUfjgsROKS0XUlw03Dj6ZoWzHGiKvbG2kJIsMxpxsYNSWBGHBLtOqfp9I4aoM=; bm_sz=BE265A55397DBD534403FF82EE82B177~YAAQtl06F92vcxeFAQAAFpGFGhIpcK+4YO2ae8IPL/cORKWoXXumRXIpXiZXdGil0JKIJmHP0IJdCXk9IWXJfrH70TC7jHpjGVhFPcfs9s37dP7+7LvsSDyW4yWsHx90bjAN1s6q6j7VOVa887wHu9GAIUG+SKNGRqvy/qKrDIpvJNI5dY8U1htNJy3tcGHpDM+/OzIImH29ns4DPh+KbSHKO4BreIdmvfAcvjFJ+qPDc+KGEsD1XknPQYf8ktlmO9Hkg37nB3alxWdb182tnPmjEgcGmqmugBXvvOSy+4e/Yx0=~3225652~3224120; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_cluster=ind1; bm_sv=9DCF9927073415AA4D83396870D0AE1B~YAAQtl06F/ixcxeFAQAAMKCFGhJShsp9gEZFchDv16yZ/MC0zMrBRsN8bDDX9gqAhf6P/M0BmP5RkCxRminv3+fK6XST6IQLE051zKFJQbuNBuSIFNCLooiOZ7GgDfwuI+n0NrdEMwmxpJcJdZ5UC1wInVjKQSe/Fr+Fn24SJYyFBoq2wim4gSzG725XDy/Roiv2rqtaOXUYsoY3l3sNZaBPBnWaMeMjTAYxK/pBN4ZVJe2T9cu7t7ddm8TbHqma~1; bm_mi=8C61EBFC5172E16BE3E395D9D257D92D~YAAQtl06F5qxcxeFAQAAoJ2FGhJVMEyVysHd4LvICG6qZXdpoacDqkCIPAMpTvX6oIW9SOc28wbJtc3ARJEqntYKhQn4EBchJQTV+nmb6wsurtvLh6NrbkkgXxpeIuYWhkOye1Us3FP/8531+wbDGfmJZ9d+dw48DGh9sd+T31FDUldVnreWWrOLIaarifroodkKSuRHP/5heR+naLjYzaS8dNIWx4bxT25evZ/Y14ZQqBeEdOeuLaCuehO8ztEi/E+ddTnmOpCXMLZpgCtFUefc9Ztr+LyAbNZv3o/tUmkA/Z94ZQq31W3HdU1uS3Lhrhs+aH8MZtvyHaU4m9K0mE1+jEffqy5nrLuX6MW2Zmh2I+KY3RDrAqxC~1; s_inv=92909; s_ivc=true; s_dur=1671187115968; s_tot_rfd=0.63; s_eng_rfd=0.00; ftv_for_gben=%252Fpc; has_consent_emea_cookie=all; tealium_user_datetime=2022-12-16t15:38:38.417; exitsurveynotdisplayed=Page%20count%20not%20met',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'fq': '',
    'text': 'laptop',
    'rows': '20',
    'sort': '',
    'display_tab': 'Products',
    'page': '2',
    'more': '1',
}

# url = 'https://www.lenovo.com/gb/en/search?text=laptop&fsid=1'
# api_url = 'https://www.lenovo.com/gb/en/search?fq=&text=laptop&rows=20&sort=&display_tab=Products&page={}&more=1'
allData = []
def cwaling_S_level(category_url,category,cat_url):
    for i in range(1,6):
        url = category_url.format(i)
        # print(url)
        # print(i)
        response = requests.get('https://www.lenovo.com/gb/en/search', params=params, headers=headers)
        soup = bs(response.text,'html.parser')
        products = soup.find_all('li','product_item')
        for product in range(len(products)):
            Pro_link = products[product].find('a').get('href')
            pro_id = Pro_link.split('/')[-1]
            Title = products[product].find('div',"product_name").text
            image = products[product].find('div','normal_image').find('img').get('src')
            price = products[product].find('div','final_price').text
            rating = products[product].find('div','star_num').text

            data ={
                'landingpage':cat_url,
                'Pro_link':Pro_link,
                'pro_id':pro_id,
                'Title':Title,
                'image':image,
                'price':price,
                'rating':rating,
                'category':category,
                'page_rank':i,
                'product_rank':product
            }    

            allData.append(data)


df=pd.read_excel('Lenovo_UK_link.xlsx',sheet_name='Sheet1')
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for count in range(len(df)):
        category_url=df['api_url'].iloc[count]
        category=df['type'].iloc[count]
        cat_url=df['category_url'].iloc[count]
        executor.submit(cwaling_S_level,category_url,category,cat_url)


df = pd.DataFrame(allData)
df.to_excel('Lenono_laptop.xlsx',index=False)
print(allData)