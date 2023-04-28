import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers["User-agent"]='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
allreview = []
def review(urlr):
    count= 1
    nextpage = urlr
    while nextpage:
        r = s.get(nextpage)
        soup = bs(r.text,'html.parser')
        # text = '||'.join([txt.text for txt in soup.find_all('div','t-ZTKy _1QgsS5')])
        review = soup.find_all('div','col _2wzgFH K0kLPL _1QgsS5')
        for i in review:
            try:
                comment = i.find('div','_6K-7Co').text
            except:
                comment = ''

            try:
                name = i.find('p','_2sc7ZR _2V5EHH _1QgsS5').text
            except:
                name = ' '

            try:
                date = i.find_all('p','_2sc7ZR')[1].text
            except:
                date = ' '
            
            try:
                Certified_Buyer = i.find('p','_2mcZGG').text
            except:
                Certified_Buyer = ' '

            try:
                like = i.find('div','_1LmwT9').text
            except:
                like = ''

            try:
                dislike = i.find('div','_1LmwT9 pkR4jH').text
            except:
                dislike = ''
            
            try:

                for imgs in i.find('div','_2nMSwX _3oLIki').find_all('div','_21YjFX _2A07HP'):
                    images = re.search('background-image:url\((.*?)\),',imgs.get('style')).group(1)
            except:
                    images = ''

            reviews = {
                'landingPage': nextpage,
                'count':count,
                'comments':comment,
                'name':name,
                'date':date,
                'Certified_Buyer':Certified_Buyer,
                'like':like,
                'dislike':dislike,
                'images':images
            }
            print(reviews)
            allreview.append(reviews)
        count+=1
        link = soup.find_all('a','_1LKTO3')
        for i in link:
            if i.text == 'Next':
                nextpage = 'https://www.flipkart.com'+i.get('href')
                # print(f'...................{nextpage}..')
                # break
            else:
                nextpage = False


url = 'https://www.flipkart.com/paduki-women-pink-flats/p/itm6ec1bdff03555?pid=SNDG69MCD3JYXNHR&lid=LSTSNDG69MCD3JYXNHRKPHXNP&marketplace=FLIPKART&store=osp%2Fiko%2F9d5&srno=b_1_8&otracker=nmenu_sub_Women_0_Flats&fm=organic&iid=en_uts6skUeJ%2FwRvzh7VpMrjB1qeb5g1E6wQcJWDMPDYcVFYEZ8Fb5acymrFPgNvhfW8SW1EeGRnqG2BJ4VZTlDuA%3D%3D&ppt=browse&ppn=browse'
# url = 'https://www.flipkart.com/titan-np2598wm03-analog-watch-women/p/itm159233d68fa7b?pid=WATFH3UJHRH9XVP5&lid=LSTWATFH3UJHRH9XVP5INS7SX&marketplace=FLIPKART&store=r18&spotlightTagId=TrendingId_r18&srno=b_1_2&otracker=nmenu_sub_Men_0_Titan&fm=organic&iid=9fd3068c-f849-4f6e-8da7-4047099e7f03.WATFH3UJHRH9XVP5.SEARCH&ppt=browse&ppn=browse&ssid=5om1ljor680000001672536397868'
urlr = url.replace('/p/','/product-reviews/')
review(urlr)
df = pd.DataFrame(allreview)
df.to_excel('flipkart_review1.xlsx',index=False)
# print(allreview)