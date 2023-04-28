from requests import Session
from lxml import html
import json, re
import pandas as pd
from bs4 import BeautifulSoup as BS
from scrapingbee import ScrapingBeeClient
import concurrent.futures
c = ScrapingBeeClient(api_key='DE592OF1RHAFV3P69R2G2127NVVFJ4RGGG159ST4X2Y0TTPYDTA9J4OKZ74E0AN4X9ZUKSUS12GC3O04')
s = Session()
s.headers['User-Agent'] ='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'

listpages = []

detailpage = []

def get_listpage_details(api_url, cat_url, category,key):
    # r = s.get(api_url)
    r = c.get(api_url,params= {'render_js':False,'wait':5000,'premium_proxy': True,'country_code':'gb',"block_resources":False})
    js = json.loads(r.text)
    total_count = int(js.get('data').get('count')/20) + 1
    api_url = api_url.replace('&page=0','&page={}')
    for page_no in range(total_count):
        r_s = s.get(api_url)
        r_s = s.get(api_url.format(page_no))
        json_data = json.loads(r_s.text)
        product_Rank = 0
        for product in json_data["data"]["data"]:
        # for product in json_data["data"]["data"][0]["products"]:
            prod_url = "https://www.lenovo.com/gb/en" + product.get('url')
            s1 = product.get('summary')
            try:
                s2 = "https:" + product['media']["heroImage"]["imageAddress"]
            except:
                s2 = ""
            try:
                s3 = '. '.join(re.findall('<li>(.*?)</li>',product.get('marketingLongDescription'))).replace('</sup>','').replace('<sup>',' ').replace('&nbsp;',' ')
            except:
                s3 = ""
            original_price = selling_price = product.get('miniPrice')
            rating_score = product.get("ratingStar")
            reviews = product.get("commentCount")
            listpages.append({"product_url": prod_url,"form_factor": category,"key":key,"S1": s1, "S2": s2, "S3": s3, 
                "Original_price": original_price, "Selling_price": selling_price, "Category_url": cat_url,"page_rank": page_no+1,
                "rating score": rating_score,"no. of reviews": reviews, "api_url" : api_url,"product_Rank":product_Rank
            })
            product_Rank+=1
        print(r_s.url)
    print(cat_url)

def get_detailpage_details(prod_url,lenovo_id):
    # r = s.get(prod_url)
    r = c.get(prod_url,params= {'render_js':True,'wait':5000,'premium_proxy': True,'country_code':'gb',"block_resources":False})
    soup = BS(r.content,'html.parser')
    tree = html.fromstring(r.content)
    # product_id = prod_url.split('/p/')[1]
    # try:
    #     bread_crumbs_in_json = json.loads(soup.find('script',attrs={'type':'application/ld+json'}).text).get('itemListElement')
    # except:
    #     bread_crumbs_in_json = json.loads(soup.find('script',attrs={'type':'application/ld+json'}).string).get('itemListElement')
    # try:
    #     bread_crumbs = ' >  '.join([name.get("name") for name in bread_crumbs_in_json])
    # except:
    bread_crumbs = '>'.join(tree.xpath('//nav[@class="breadcrumb clearfix"]//ol//li//a//text()'))
    # images = '| '.join(['https://www.lenovo.com'+''.join(i.xpath('./@src')) for i in tree.xpath('//div[@class="gallery-image-slider"]//div[@class="slick-slide"]//img')])
    try:
        p1 = ''.join(tree.xpath('//meta[@name="productInfo.name"]/@content'))
    except:
        p1 = ''.join(tree.xpath('//meta[@name="productInfo.name"]/@content'))
    try:
        images = ''.join(tree.xpath('//meta[@name="thumbnail"]/@content'))
    except:
        images = ''.join(tree.xpath('//meta[@name="thumbnail"]/@content'))
    try:
        p3 = ''.join(tree.xpath('//div[@class="banner_content_desc"]//p//text()'))
    except:
        p3 = ''.join(tree.xpath('//div[@class="banner_content_desc"]//p//text()'))
    try:
        price = ''.join(tree.xpath('//meta[@name="productpromotionprice"]/@content'))
    except:
        price = ''.join(tree.xpath('//meta[@name="productpromotionprice"]/@content'))
    block_data = ''.join(tree.xpath('//table//tr//text()')).strip()
    processor = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Processor")]//following-sibling::p//text()'))
    os = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Operating System")]//following-sibling::p//text()'))
    Memory = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Memory")]//following-sibling::p//text()'))
    Storage = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Storage")]//following-sibling::p//text()'))
    Display = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Display")]//following-sibling::p//text()'))
    Battery = ''.join(tree.xpath('//div[@class="system_specs_container"]//ul//li[contains(string(),"Battery")]//following-sibling::p//text()'))
    Camera = ''.join(tree.xpath('//table//tr//th[contains(string(),"Camera")]//following-sibling::td//p//text()'))
    # if bool(rating) == False:
    #     rating_api = "https://api.bazaarvoice.com/data/statistics.json?apiversion=5.4&passkey=caTO1uXNBEd1aZR9OV3g6hbHlGDmdinXzAKQqxNI6GnZw&stats=Reviews&filter=ContentLocale:en_GB,en_AU,en_NZ,en_MY,en_SG,en_IN,en_CA,en_US,en_HK,en_TW,en_TH,en_DK,en_NL,en_SE,en_BR&filter=ProductId:{}"
    #     r_s = s.get(rating_api.format(product_id))
    #     js = json.loads(r_s.text)
    #     if bool(js.get("Results")) == False:
    #         rating = ""
    #         reviews = ""
    #     else:
    #         if js.get('Results')[0].get('ProductStatistics').get('ReviewStatistics').get("AverageOverallRating") == None:
    #             rating = ""
    #         else:
    #             rating = "{:.1f}".format(float(js.get('Results')[0].get('ProductStatistics').get('ReviewStatistics').get("AverageOverallRating")))
    #             reviews = js.get('Results')[0].get('ProductStatistics').get('ReviewStatistics').get("TotalReviewCount")
    try:
        stock = re.search('"availability":"http://schema.org/(.*?)"',r.text).group(1)
    except:
        stock = ""
    detail_page = {
        "OEM" : "Lenovo",
        "Country" : "AU",
        # "product_id" : product_id,
        # "form_factor" : category,
        # "category_url" : cat_url,
        "product_url" : prod_url,
        # "S1 - product_title" : s1,
        # "S2 - image_url" : s2,
        # "S3 - Specifications" : s3,
        "P1-product_title" : p1,
        "P2-image_url" : images,
        "Lenovo_id": lenovo_id,
        "P3 - Specifications" : p3,
        # "page_rank" : page_rank,
        # "product_Rank" : product_Rank,
        "original_price" : price,
        "sellling_price" : price,
        "Stock info" : stock,
        "processor" :processor,
        "graphic_card" : "",
        "Breadcrumbs" : bread_crumbs,
        "Block Data" : block_data,
        "OS" : os,
        "Battery": Battery,
        "display" : Display,
        "Memory" : Memory,
        "Storage" : Storage,
        "Camera" : Camera,
        # "rating score" : rating,
        # "no. of reviews" : reviews
    }
    detailpage.append(detail_page)
    print(prod_url)


input_file = pd.read_excel("Lenovo_UK_panding_url.xlsx", sheet_name='Sheet1',engine='openpyxl')
for count in range(len(input_file)):
    api_url = input_file.iloc[count]['api']
    cat_url = input_file.iloc[count]['url']
    category = input_file.iloc[count]['type']
    key = input_file.iloc[count]['key']

    get_listpage_details(api_url, cat_url, category,key)

print('Listpage Completed')
print(f"Found {len(listpages)} Products from Listpage")
df = pd.DataFrame(listpages)
df.to_excel('lispage_uk.xlsx',index=False)

df_read = pd.read_excel('Lenovo_Uk_S_Level_1.xlsx', sheet_name="Sheet2",engine='openpyxl')
print(df_read)
# for count in range(len(df_read)):
#     prod_url = df_read['product_url'].iloc[count]
#     category = df_read["form_factor"].iloc[count]
#     s1 = df_read["S1"].iloc[count]
#     s2 = df_read["S2"].iloc[count]
#     s3 = df_read["S3"].iloc[count]
#     # original_price = df_read.iloc[count].get("Original_price")
#     cat_url = df_read["Category_url"].iloc[count]
#     page_rank = df_read["page_rank"].iloc[count]
#     rating = df_read["rating score"].iloc[count]
#     reviews = df_read["no. of reviews"].iloc[count]
#     prd_rank = df_read["product_Rank"].iloc[count]
#     get_detailpage_details(prod_url, category, s1, s2, s3, cat_url, page_rank, rating, reviews,prd_rank)

with concurrent.futures.ThreadPoolExecutor(max_workers =10) as executor:
    for count in range(len(df_read)):
        prod_url = df_read['Product URL'].iloc[count]
        lenovo_id= df_read['Lenovo_id'].iloc[count]
        # category = df_read["form_factor"].iloc[count]
        # s1 = df_read["S1"].iloc[count]
        # s2 = df_read["S2"].iloc[count]
        # s3 = df_read["S3"].iloc[count]
        # cat_url = df_read["Category_url"].iloc[count]
        # page_rank = df_read["page_rank"].iloc[count]
        # rating = df_read["rating score"].iloc[count]
        # reviews = df_read["no. of reviews"].iloc[count]
        # prd_rank = df_read["product_Rank"].iloc[count]
        executor.submit(get_detailpage_details,prod_url,lenovo_id)


df = pd.DataFrame(detailpage)
df.to_csv("lenovo_uk_detail.csv",index=False)