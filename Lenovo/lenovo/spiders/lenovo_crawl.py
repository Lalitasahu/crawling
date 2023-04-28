import scrapy
import pandas as pd
from scrapy.http import Request
# from read_files  import read_csv, read_excel

class LenovoCrawlSpider(scrapy.Spider):
    name = "lenovo_crawl"
    allowed_domains = ["*"]
    # start_urls = ["http://lenovo.com/"]
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:109.0) Gecko/20100101 Firefox/110.0'}
    
    def start_requests(self):
        df = pd.read_excel('./Lenovo/lenovo_urls.xlsx')
        print(df)
        for w in range(len(df)):
        # for w in range(2):
            row = df.iloc[w].to_dict()
            yield scrapy.Request(row['Landing_url'],callback=self.apihits, dont_filter=True, headers=self.headers, meta={'Landing_url':row['Landing_url']})

    def start_requests(self, response):
        # cat_Id = response.url.split(':')[-1]
        Landing_url = response.meta.get('Landing_url')
        df = pd.read_excel('./Lenovo/lenovo_urls.xlsx')
        for i in range(len(df)):
        # for i in range(2):
            row = df.iloc[i].to_dict()
            yield scrapy.Request(row['API_Url'],callback=self.listpage, dont_filter=True,headers=self.headers, meta={'Landing_url':Landing_url})
    
    def listpage(self, response):
        Landing_url = response.meta.get('Landing_url')
        js = response.json()
        if js:
            products = js['data']['data']
        else:
            products =  js['data']['data'][0]['products']
        page = 1
        for product in range(len(products)):
            id = products[product].get('id')
            name = products[product].get('productName')
            pro_url = 'https://www.lenovo.com/us/en'+products[product].get('url')
            pro_code = products[product].get('productCode')
            price = products[product].get('miniPrice')
            ratingStar = products[product].get('ratingStar')
            commentCount = products[product].get('commentCount')
            marketingShortDescription = products[product].get('marketingShortDescription')
            image = 'https:'+products[product].get('media').get('listImage')[0].get('imageAddress')
            # print(image)
            yield {
                'landingPage':Landing_url,
                'product_rank': product,
                'page_rank':page+1,
                'id':id,
                'name':name,
                'pro_url':pro_url,
                'pro_code':pro_code,
                'price':price,
                'ratingStar':ratingStar,
                'commentCount':commentCount,
                'marketingShortDescription':marketingShortDescription,
                'image':image
                
            }
