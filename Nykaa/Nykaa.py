import requests
import re 
import pandas as pd
from lxml import html
from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

def detailPage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')
    tree = html.fromstring(r.text)
    try:
        ratings = soup.find('div','css-1hvvm95').text.replace('\xa0','')
    except:
        ratings =' '
    try:
        reviews = tree.xpath('//div[@class="css-1hvvm95"]//text()')[-2]
    except:
        reviews =' '

    try:
        quantity =soup.find('span','css-pzbce3').text
    except:
        quantity = ''

    try:   
        img = soup.find_all('img',{'alt':'product-thumbnail'})
        allimages = []
        for i in img:
            imgs = i.get('src')
            allimages.append(imgs)
    except:
            allimages=''

    try:
        ingredients =  re.search('"ingredients":"(.*?)",',r.text).group(1).replace('</p>','').replace('<p><b>','')
    except:
        ingredients =''

    try:
        howtoUse =  re.search('"howToUse":"(.*?)"',r.text).group(1).replace('<p>','').replace('</p>','')
    except:
        howtoUse = ' '


    data = {
        'ratings':ratings,
        'reviews':reviews,
        'quantity':quantity,
        'images':allimages,
        'ingredients':ingredients,
        'howtoUse':howtoUse
    }
    print(data)
    return data

alldata = []
def listpage():
    url = 'https://www.nykaa.com/skin/moisturizers/night-cream/c/8395?page_no={}&sort=popularity&eq=desktop'
    # url = 'https://www.nykaa.com/hair-care/hair/shampoo/c/316?page_no={}&sort=popularity&ptype=lst&id=316&root=nav_3&dir=desc&order=popularity&eq=desktop'
    for i in range(1,39): # find the execet 
        urls = url.format(i)
        r = s.get(urls)
        print(r.url)
        soup = bs(r.text,'html.parser')
        products = soup.find_all('div','productWrapper')
        for product in products:
            try:
                Name = product.find('div','css-xrzmfa').text
            except:
                Name =""

            try:
                pro_Url = 'https://www.nykaa.com'+product.find('a','css-qlopj4').get('href')
            except:
                pro_Url = ""

            try:
                list_Price = product.find('span','css-17x46n5').text
            except:
                list_Price = ''

            try:
                Selling_price = product.find('span','css-111z9ua').text
            except:
                Selling_price = ''

            try:
                Off = product.find('span','css-r2b2eh').text
            except:
                Off = ''

            try:
                review = product.find('span','css-1j33oxj').text
            except:
                review = ''

            detail = detailPage(pro_Url)
            # print(pro_Url)
            data = {
                'landingUrl':url,
                'Name':Name,
                'pro_Url':pro_Url,
                'list_Price':list_Price,
                'Selling_price':Selling_price,
                'Off':Off,
                'review':review

            }
            data.update(detail)
            # print(data)
            alldata.append(data)

listpage()
df = pd.DataFrame(alldata)
df.to_excel('Nykaa1.xlsx',index=False)