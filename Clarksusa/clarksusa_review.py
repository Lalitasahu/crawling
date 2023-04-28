import requests 
import re
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import session
s = session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'



allreviews = []
def review():
    offset = 0
    nextpage = True
    while nextpage:
        url = f'https://api.bazaarvoice.com/data/batch.json?passkey=b5sbvchuo8alfvu32evh0bnug&apiversion=5.5&displaycode=19244-en_us&resource.q0=reviews&filter.q0=isratingsonly:eq:false&filter.q0=productid:eq:26124663&filter.q0=contentlocale:eq:en_EU,en_US&sort.q0=submissiontime:desc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors,products,comments&filter_reviews.q0=contentlocale:eq:en_EU,en_US&filter_reviewcomments.q0=contentlocale:eq:en_EU,en_US&filter_comments.q0=contentlocale:eq:en_EU,en_US&limit.q0=30&offset.q0={offset}&limit_comments.q0=3&'
        r = s.get(url)
        # print(r.url)
        js = r.json()
        # print(js)
        totalcount = js['BatchedResults']['q0']['TotalResults']
        print(totalcount)
        if offset >= totalcount:
            nextpage = False

        allrevew = js['BatchedResults']['q0']['Results']
        for reviews  in allrevew:
            Title = reviews.get('Title')
            Name = reviews.get('UserNickname')
            comment = reviews.get('ReviewText')
            Rating = reviews.get('RatingRange')
            photo = reviews.get('Photos')
        
            data ={
                'landingUrl':url, # change
                'Title':Title,
                'Name':Name,
                'comment':comment,
                'Rating':Rating,
                'photo':photo
            }
            allreviews.append(data)
            print(data)
        if offset == 0 :
            offset +=8
        else:
            offset +=30
url = 'https://www.clarksusa.com/c/Arla-Glison/p/26124663'

review()