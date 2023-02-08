from ast import excepthandler
from hashlib import shake_128
# from unicodedata import category
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
from scrapingbee import ScrapingBeeClient
import pandas as pd
import concurrent.futures
from xlsxwriter import Workbook
import re
import pandas as pd
c = ScrapingBeeClient(api_key='DE592OF1RHAFV3P69R2G2127NVVFJ4RGGG159ST4X2Y0TTPYDTA9J4OKZ74E0AN4X9ZUKSUS12GC3O04')

pdp_data = []

# def crawling_P_level(prod_url):
def crawling_P_level(url):
    c = ScrapingBeeClient(api_key='DE592OF1RHAFV3P69R2G2127NVVFJ4RGGG159ST4X2Y0TTPYDTA9J4OKZ74E0AN4X9ZUKSUS12GC3O04')
    r = c.get(url,params= {'render_js':True,'wait':5000,'premium_proxy': True,'country_code':'us',"block_resources":False})
    # r = c.get(prod_url,params= {'render_js':True,'wait':5000,'premium_proxy':False,'country_code':'us',"block_resources":False})
    # r = c.get(prod_url,params= {'wait':5000,'stealth_proxy':False,'country_code':'us',"block_resources":False})
    # if r.status_code == 200:
    soup = bs(r.content,"html.parser")
    tree=html.fromstring(r.text)
    # if tree.xpath("//meta[@name='thumbnail']//@content"):
    P2 = ''.join(tree.xpath("//div[@class='image-pic']//img/@src | //meta[@name='thumbnail']//@content"))
    # elif tree.xpath('//div[@class="image-pic"]//img/@src'):
    #     P2 = '|'.join(set(tree.xpath('//div[@class="image-pic"]//img/@src')))
    # else:
    #     P2 = ""

    try:
        breadcrumbs = '>'.join(tree.xpath('//nav[@class="breadcrumb clearfix"]//li//a//text()'))
    except:
        breadcrumbs = '>'.join(tree.xpath('//nav[@class="breadcrumb clearfix"]//li//a//text()'))
    try:
        P1 = ''.join(tree.xpath("//h2[@class='product_summary']//text() | //div[@class='banner_content_desc']//h3//text()"))
    except:
        P1 = ''.join(tree.xpath("//h2[@class='product_summary']//text() | //div[@class='banner_content_desc']//h3//text()"))
    try:
        P3 = ' '.join(tree.xpath("//div[@class='banner_content_desc']//ul//li//text()"))
    except:
        P3 = ' '.join(tree.xpath("//div[@class='banner_content_desc']//ul//li//text()"))
    
    # if tree.xpath('//meta[@name="productprice"]/@content'):
    #     sellling_price = ''.join(tree.xpath('//meta[@name="productprice"]/@content'))
    if tree.xpath('//meta[@name="productpromotionprice"]/@content'):
        sellling_price = ''.join(tree.xpath('//meta[@name="productpromotionprice"]/@content'))
    elif re.search('"price":(.*?)},"name"',r.text):
        sellling_price = re.search('"price":(.*?)},"name"',r.text).group(1)
    else:
        sellling_price = ""

    original_price = ''.join(tree.xpath('//meta[@name="productprice"]/@content'))

    product_id = url.split("/")[-1]
    try:
        stock = re.search('"availability":"http://schema.org/(.*?)"',r.text).group(1)
    except:
        stock = ""
    try:
        processor = ''.join(tree.xpath("//div[@class='specs-inner']//tr//th[contains(string(),'Processor')]//ancestor::tr//following-sibling::td//text() | //div[@class='system_specs_container']//ul//li//div[contains(string(),'Processor')]//following-sibling::p//text() | //meta[@name='Processor']/@content"))
    except:
        processor = ''.join(tree.xpath("//div[@class='specs-inner']//tr//th[contains(string(),'Processor')]//ancestor::tr//following-sibling::td//text() | //div[@class='system_specs_container']//ul//li//div[contains(string(),'Processor')]//following-sibling::p//text() | //meta[@name='Processor']/@content"))
    try:    
        graphics = ''.join(tree.xpath("//div[@class='system_specs_container']//ul//li//div[contains(string(),'Graphic Card')]//following-sibling::p//text() | //div[@class='specs-inner']//tr//th[contains(string(),'Graphics')]//ancestor::tr//following-sibling::td//text() | //div[@class='system_specs_container']//ul//li//div[contains(string(),'Graphics')]//following-sibling::p//text() | //table//th[contains(string(),'Graphics')]//ancestor::th//following-sibling::td//text()")).replace("\xa0Xe","")
    except:
        graphics = ''.join(tree.xpath("//div[@class='specs-inner']//tr//th[contains(string(),'Graphics')]//ancestor::tr//following-sibling::td//text() | //div[@class='system_specs_container']//ul//li//div[contains(string(),'Graphics')]//following-sibling::p//text() | //table//th[contains(string(),'Graphics')]//ancestor::th//following-sibling::td//text()")).replace("\xa0Xe","")
    try:
        Memory = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Memory")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Memory")]//following-sibling::p//text() | //table//th[contains(string(),"Memory")]//ancestor::th//following-sibling::td//text()')).strip()
    except:
        Memory = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Memory")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Memory")]//following-sibling::p//text() | //table//th[contains(string(),"Memory")]//ancestor::th//following-sibling::td//text()')).strip()
    try:
        Storage = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Storage")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Storage")]//following-sibling::p//text() | //table//th[contains(string(),"Storage")]//ancestor::th//following-sibling::td//text()')).strip()
    except:
        Storage = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Storage")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Storage")]//following-sibling::p//text() | //table//th[contains(string(),"Storage")]//ancestor::th//following-sibling::td//text()')).strip()

        # ---
    # Color = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Color")]//following-sibling::td//p//text()')).strip()
    # Battery = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Battery")]//following-sibling::td//p//text()')).strip()
    # Weight = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Weight")]//following-sibling::td//p//text()')).strip()
    # ---
    try:
        Display = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Display")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Display")]//following-sibling::p//text() | //table//th[contains(string(),"Display")]//ancestor::th//following-sibling::td//text()')).strip()
    except:
        Display = ''.join(tree.xpath('//div[@class="specs-inner"]//table//tr//th[contains(string(),"Display")]//following-sibling::td//p//text() | //div[@class="system_specs_container"]//ul//li//div[contains(string(),"Display")]//following-sibling::p//text() | //table//th[contains(string(),"Display")]//ancestor::th//following-sibling::td//text()')).strip()
    try:
        review = ''.join(tree.xpath("//div[@class='review-inline']//div[@class='bv_numReviews_component_container']//div[@class='bv_text']//text() | //h2[@class='product_summary']//following-sibling::div[@class='rating-container']//@data-review-count"))
    except:
        review = ''.join(tree.xpath("//h2[@class='product_summary']//following-sibling::div[@class='rating-container']//@data-review-count"))
    try:
        rating = ''.join(tree.xpath("//div[@class='review-inline']//div[@class='bv_averageRating_component_container']//div//text() | //h2[@class='product_summary']//following-sibling::div[@class='rating-container']//@data-rating-star"))
    except:
        rating = ''.join(tree.xpath("//h2[@class='product_summary']//following-sibling::div[@class='rating-container']//@data-review-count"))
        stk = re.findall(',"availability":"(.*?)",',r.text)
        if "instock" or "in stock" in stk[0].lower():
            stock = "In stock"
        else:
            stock = "Out stock"
    f_mpn = re.findall(',"mpn":"(.*?)",',r.text)
    mpn = f_mpn[0] if f_mpn else ""
    f_sku = re.findall(',"sku":"(.*?)"}',r.text)
    sku = f_sku[0] if f_sku else ""
    block_Data = ' '.join(tree.xpath("//div[@class='system_specs_container']//ul//li//text()")).replace('  ','').replace('\n','').replace('\t','')
    d={}
    # d["Land_page_url"]= land_pge
    d["prod_url"] = url
    # d["pro_id"] = pro_id
    d["breadcrumbs"] =breadcrumbs
    d["sellling_price"] =sellling_price
    d["original_price"] = original_price
    # d["specifications"] =specifications
    d["P1"] =P1
    d["P2"] = P2
    d["P3"]= P3
    d["processor"] = processor
    d["graphics"] = graphics
    d["Memory"] = Memory
    d["stock"] = stock 
    d["Storage"] = Storage
    d["product_id"] = product_id
    d["MPN"] = mpn
    d['processor'] = processor
    d["Display"] = Display
    d["block_Data"] = block_Data
    d["review"] = review
    d["rating"] = rating
    pdp_data.append(d)
    print(d)



df = pd.read_excel("Lenovo_us_urls.xlsx", sheet_name='Sheet1',engine='openpyxl')
print(df)
with concurrent.futures.ThreadPoolExecutor(max_workers =10) as executor:
    for i in range(len(df)):
    # for i in range(20):
        cb = df.iloc[i] 
        url = str(cb["pro_url"])
        # pro_id =str(c["pro_id"])
        executor.submit(crawling_P_level,url)
# for i in range(len(df)):
# # for i in range(20):
#     c = df.iloc[i] 
#     url = str(c["Pro_link"])
#     pro_id =str(c["pro_id"])
#     crawling_P_level(url,pro_id)

prd_data = pd.DataFrame(pdp_data)
writer = pd.ExcelWriter("Lenovo_us_P_level_data.xlsx",engine='xlsxwriter')
prd_data.to_excel(writer,sheet_name='Plevel Data',index=False) 
writer.close()

