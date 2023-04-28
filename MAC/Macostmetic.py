import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import Session
import re
s = Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.maccosmetics.in/',
    'Content-Type': 'application/json',
    'business-unit': '2-mc-in-en-ecommv1',
    'Cache-Control': 'no-cache',
    'ClientId': 'stardust-fe-client',
    'authorizationtoken': 'Mi1tYy1pbi1lbi1lY29tbXYxOmh0dHBzOi8vd3d3Lm1hY2Nvc21ldGljcy5pbg==',
    'Origin': 'https://www.maccosmetics.in',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'query': '{\n                products(environment: {prod:true},\n                    filter: [{tags:{filter:{id:{in:["13854"]}},includeInnerHits:false}}],\n                    sort: [{tags:{product_display_order:ASCENDING}}]\n                ) {\n                    \n        ... product__collection \n        \n        items {\n            ... product_default ... product_productSkinType ... product_form ... product_productCoverage ... product_benefit ... product_productReview ... product_skinConcern ... product_usage ... product_productFinish ... product_usageOptions ... product_brushTypes ... product_brushShapes \n            skus {\n                total\n                items {\n                    ... product__skus_default ... product__skus_autoReplenish ... product__skus_perlgem ... product__skus_colorFamily ... product__skus_skuLargeImages ... product__skus_skuMediumImages ... product__skus_skuSmallImages ... product__skus_vtoFoundation ... product__skus_vtoMakeup \n                }\n            }\n        }\n    \n    \n                }\n            }\n\nfragment product__collection \n    on product_collection {\n        items {\n            product_id\n            skus {\n                items {\n                    inventory_status\n                    sku_id\n                }\n            }\n        }\n    }\n\n\nfragment product_default \n    on product {\n        default_category {\n            id\n            value\n        }\n        description\n        display_name\n        is_hazmat\n        meta {\n            description\n        }\n        product_badge\n        product_id\n        product_url\n        short_description\n        tags {\n            total\n            items {\n                id\n                value\n                key\n            }\n        }\n    }\n\n\nfragment product_productSkinType \n    on product {\n        skin {\n            type {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_form \n    on product {\n        form {\n            key\n            value\n        }\n    }\n\n\nfragment product_productCoverage \n    on product {\n        coverage {\n            key\n            value\n        }\n    }\n\n\nfragment product_benefit \n    on product {\n        benefit {\n            benefits {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_productReview \n    on product {\n        reviews {\n            average_rating\n            number_of_reviews\n        }\n    }\n\n\nfragment product_skinConcern \n    on product {\n        skin {\n            concern {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_usage \n    on product {\n        usage {\n            content\n            label\n            type\n        }\n    }\n\n\nfragment product_productFinish \n    on product {\n        finish {\n            key\n            value\n        }\n    }\n\n\nfragment product_usageOptions \n    on product {\n        usage_options {\n            key\n            value\n        }\n    }\n\n\nfragment product_brushTypes \n    on product {\n        brush {\n            types {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_brushShapes \n    on product {\n        brush {\n            shapes {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product__skus_default \n    on product__skus {\n        is_default_sku\n        is_discountable\n        is_giftwrap\n        is_under_weight_hazmat\n        iln_listing\n        iln_version_number\n        inventory_status\n        material_code\n        prices {\n            currency\n            is_discounted\n            include_tax {\n                price\n                original_price\n                price_per_unit\n                price_formatted\n                original_price_formatted\n                price_per_unit_formatted\n            }\n        }\n        sizes {\n            value\n            key\n        }\n        shades {\n            name\n            description\n            hex_val\n        }\n        sku_id\n        sku_badge\n        unit_size_formatted\n        upc\n    }\n\n\nfragment product__skus_autoReplenish \n    on product__skus {\n        is_replenishable\n    }\n\n\nfragment product__skus_perlgem \n    on product__skus {\n        perlgem {\n            SKU_BASE_ID\n        }\n    }\n\n\nfragment product__skus_colorFamily \n    on product__skus {\n        color_family {\n            key\n            value\n        }\n    }\n\n\nfragment product__skus_skuLargeImages \n    on product__skus {\n        media {\n            large {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_skuMediumImages \n    on product__skus {\n        media {\n            medium {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_skuSmallImages \n    on product__skus {\n        media {\n            small {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_vtoFoundation \n    on product__skus {\n        vto {\n            is_foundation_experience\n        }\n    }\n\n\nfragment product__skus_vtoMakeup \n    on product__skus {\n        vto {\n            is_color_experience\n        }\n    }\n',
    'variables': {},
}

# review api ='https://display.powerreviews.com/m/269258/l/all/product/52593/reviews?apikey=1d01c6a1-3fb0-429d-9b01-7b3d915933af&_noconfig=true&page_locale=en_IN'

def detailpage(url):
    r = s.get(url)
    soup = bs(r.text,'html.parser')

    try:
        price = soup.find('span','product-price js-product-price').text
    except:
        price = ''

    try:
        shortdescritption = soup.find('h2','product-full__short-desc').text
    except:
        shortdescritption = ''

    try:
        longdescription = soup.find('div','product-overview--description js-product-overview-desc').text
    except:
        longdescription = ''

    
    try:
        Benefit = soup.find('div',{'id':"product-overview--about"}).text
    except:
        Benefit =''
    
    try:
        Ingredients = soup.find('span','sku-ingredients js-sku-ingredients').text
    except:
        Ingredients = " "

    try:
        RECOMMENDED = soup.find('div',{'id':'product-overview--product_usage'}).text
    except:
        RECOMMENDED = " "
    
    allImg=soup.find_all('figure','basic-landscape-tout-v1')
    imges = ''
    for i in allImg:
        imges = i.find('img').get('data-src')
        

    data = {
        'price':price,
        'shortdescritption':shortdescritption,
        'longdescription':longdescription,
        'Benefit':Benefit,
        'Ingredients':Ingredients,
        'RECOMMENDED':RECOMMENDED,
        'imges':imges

    }
    
    return data



alldata = []


def listpage(url):
    # r = s.get(url)
    # try:
    #     id = url.split('products/')[0].split('/')[-2] #Lipstick
    # except:
    #     id = url.split('products/')[1].replace('/','')  # other
    id = re.search('\d+',url).group(0) # \d is use for the number 
    json_data = {
    'query': '{\n                products(environment: {prod:true},\n                    filter: [{tags:{filter:{id:{in:["__ID__"]}},includeInnerHits:false}}],\n                    sort: [{tags:{product_display_order:ASCENDING}}]\n                ) {\n                    \n        ... product__collection \n        \n        items {\n            ... product_default ... product_productSkinType ... product_form ... product_productCoverage ... product_benefit ... product_productReview ... product_skinConcern ... product_usage ... product_productFinish ... product_usageOptions ... product_brushTypes ... product_brushShapes \n            skus {\n                total\n                items {\n                    ... product__skus_default ... product__skus_autoReplenish ... product__skus_perlgem ... product__skus_colorFamily ... product__skus_skuLargeImages ... product__skus_skuMediumImages ... product__skus_skuSmallImages ... product__skus_vtoFoundation ... product__skus_vtoMakeup \n                }\n            }\n        }\n    \n    \n                }\n            }\n\nfragment product__collection \n    on product_collection {\n        items {\n            product_id\n            skus {\n                items {\n                    inventory_status\n                    sku_id\n                }\n            }\n        }\n    }\n\n\nfragment product_default \n    on product {\n        default_category {\n            id\n            value\n        }\n        description\n        display_name\n        is_hazmat\n        meta {\n            description\n        }\n        product_badge\n        product_id\n        product_url\n        short_description\n        tags {\n            total\n            items {\n                id\n                value\n                key\n            }\n        }\n    }\n\n\nfragment product_productSkinType \n    on product {\n        skin {\n            type {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_form \n    on product {\n        form {\n            key\n            value\n        }\n    }\n\n\nfragment product_productCoverage \n    on product {\n        coverage {\n            key\n            value\n        }\n    }\n\n\nfragment product_benefit \n    on product {\n        benefit {\n            benefits {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_productReview \n    on product {\n        reviews {\n            average_rating\n            number_of_reviews\n        }\n    }\n\n\nfragment product_skinConcern \n    on product {\n        skin {\n            concern {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_usage \n    on product {\n        usage {\n            content\n            label\n            type\n        }\n    }\n\n\nfragment product_productFinish \n    on product {\n        finish {\n            key\n            value\n        }\n    }\n\n\nfragment product_usageOptions \n    on product {\n        usage_options {\n            key\n            value\n        }\n    }\n\n\nfragment product_brushTypes \n    on product {\n        brush {\n            types {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product_brushShapes \n    on product {\n        brush {\n            shapes {\n                key\n                value\n            }\n        }\n    }\n\n\nfragment product__skus_default \n    on product__skus {\n        is_default_sku\n        is_discountable\n        is_giftwrap\n        is_under_weight_hazmat\n        iln_listing\n        iln_version_number\n        inventory_status\n        material_code\n        prices {\n            currency\n            is_discounted\n            include_tax {\n                price\n                original_price\n                price_per_unit\n                price_formatted\n                original_price_formatted\n                price_per_unit_formatted\n            }\n        }\n        sizes {\n            value\n            key\n        }\n        shades {\n            name\n            description\n            hex_val\n        }\n        sku_id\n        sku_badge\n        unit_size_formatted\n        upc\n    }\n\n\nfragment product__skus_autoReplenish \n    on product__skus {\n        is_replenishable\n    }\n\n\nfragment product__skus_perlgem \n    on product__skus {\n        perlgem {\n            SKU_BASE_ID\n        }\n    }\n\n\nfragment product__skus_colorFamily \n    on product__skus {\n        color_family {\n            key\n            value\n        }\n    }\n\n\nfragment product__skus_skuLargeImages \n    on product__skus {\n        media {\n            large {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_skuMediumImages \n    on product__skus {\n        media {\n            medium {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_skuSmallImages \n    on product__skus {\n        media {\n            small {\n                src\n                alt\n                height\n                width\n            }\n        }\n    }\n\n\nfragment product__skus_vtoFoundation \n    on product__skus {\n        vto {\n            is_foundation_experience\n        }\n    }\n\n\nfragment product__skus_vtoMakeup \n    on product__skus {\n        vto {\n            is_color_experience\n        }\n    }\n'.replace('__ID__', id),
    'variables': {},
    }
    # print(json_data)
    

    response = requests.post('https://emea.sdapi.io/stardust-prodcat-product-v3/graphql/core/v1/extension/v1',headers=headers,json=json_data)
    js = response.json()
    # print(js)
    products =js['data']['products']['items']
    for product in products:
        name = product.get('display_name')
        Product_id = product.get('product_id')
        Product_URL = 'https://www.maccosmetics.in'+product.get('product_url')
        Average_rating = product.get('average_rating')
        Number_of_reviews = product.get('number_of_reviews')
        image = product.get('skus').get('items')
        images = []
        for im in image:
            img = im.get('media').get('large')
            for i in img:
                imgs = i.get('src')
                images.append(imgs)
        detail = detailpage(Product_URL)
        # print(Number_of_reviews)

        data = {
            'Product_id':Product_id,
            'Product_URL':Product_URL,
            # 'number_of_reviews':Number_of_reviews,
            # 'Average_rating':Average_rating,
            # 'images':images
        }
        data.update(detail)
        alldata.append(data)
        print(alldata)


# url = 'https://www.maccosmetics.in/products/27772/products/makeup/eyes/kajal'
url = "https://www.maccosmetics.in/products/13854/products/Makeup/Lips/Lipstick"
# url = 'https://www.maccosmetics.in/products/27854/products/skincare/prep-prime-fix'

listpage(url)
df = pd.DataFrame(alldata)
df.to_excel('Macecostmetics.xlsx',index=False)


