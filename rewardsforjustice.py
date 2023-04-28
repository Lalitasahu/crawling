import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from requests import Session
s = Session()


cookies = {
    '_ga_BPR2J8V0QK': 'GS1.1.1681369264.1.1.1681372963.0.0.0',
    '_ga': 'GA1.1.1456016636.1681369264',
    'wp-wpml_current_language': 'en',
    'cookie_notice_accepted': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://rewardsforjustice.net',
    'Connection': 'keep-alive',
    'Referer': 'https://rewardsforjustice.net/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074&pagenum=2',
    # 'Cookie': '_ga_BPR2J8V0QK=GS1.1.1681369264.1.1.1681372963.0.0.0; _ga=GA1.1.1456016636.1681369264; wp-wpml_current_language=en; cookie_notice_accepted=true',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
    'action': 'jet_smart_filters',
    'provider': 'jet-engine/rewards-grid',
    'query[_tax_query_crime-category][]': [
        '1070',
        '1071',
        '1073',
        '1072',
        '1074',
    ],
    'defaults[post_status][]': 'publish',
    'defaults[post_type][]': [
        'north-korea',
        'rewards',
    ],
    'defaults[posts_per_page]': '9',
    'defaults[paged]': '1',
    'defaults[ignore_sticky_posts]': '1',
    'settings[lisitng_id]': '22078',
    'settings[columns]': '3',
    'settings[columns_tablet]': '1',
    'settings[columns_mobile]': '1',
    'settings[post_status][]': 'publish',
    'settings[use_random_posts_num]': '',
    'settings[posts_num]': '9',
    'settings[max_posts_num]': '',
    'settings[not_found_message]': 'No data was found',
    'settings[is_masonry]': '',
    'settings[equal_columns_height]': '',
    'settings[use_load_more]': '',
    'settings[load_more_id]': '',
    'settings[load_more_type]': 'click',
    'settings[load_more_offset][unit]': 'px',
    'settings[load_more_offset][size]': '0',
    'settings[loader_text]': '',
    'settings[loader_spinner]': '',
    'settings[use_custom_post_types]': 'yes',
    'settings[custom_post_types][]': [
        'north-korea',
        'rewards',
    ],
    'settings[hide_widget_if]': '',
    'settings[carousel_enabled]': '',
    'settings[slides_to_scroll]': '3',
    'settings[arrows]': 'true',
    'settings[arrow_icon]': 'fa fa-angle-left',
    'settings[dots]': '',
    'settings[autoplay]': '',
    'settings[autoplay_speed]': '5000',
    'settings[infinite]': '',
    'settings[center_mode]': '',
    'settings[effect]': 'slide',
    'settings[speed]': '500',
    'settings[inject_alternative_items]': '',
    'settings[injection_items][0][item]': '90086',
    'settings[injection_items][0][_id]': 'a4c8515',
    'settings[injection_items][0][item_num]': '1',
    'settings[injection_items][0][inject_once]': 'yes',
    'settings[injection_items][0][meta_key]': 'dprk',
    'settings[injection_items][0][item_condition_type]': 'item_meta',
    'settings[injection_items][0][static_item]': 'yes',
    'settings[scroll_slider_enabled]': '',
    'settings[scroll_slider_on][]': [
        'desktop',
        'tablet',
        'mobile',
    ],
    'settings[custom_query]': '',
    'settings[custom_query_id]': '',
    'settings[_element_id]': 'rewards-grid',
    'settings[jet_cct_query]': '',
    'settings[jet_rest_query]': '',
    'props[found_posts]': '181',
    'props[max_num_pages]': '21',
    'props[page]': '1',
    'paged': '2',
    'referrer[uri]': '/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074&pagenum=1',
    'referrer[info]': '',
    'referrer[self]': '/index.php',
    'indexing_filters': '[41852,41851]',
}

def detailpage(url):
     



def listpage():
    page_number = 1
    nextpage = True
    while nextpage:
        response = requests.post('https://rewardsforjustice.net/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        print(response)
        js = response.json()

        if js['pagination']['max_num_pages'] >= page_number:
            data['paged'] = str(page_number+1) 
        
        soup = bs(js['content'],'html.parser')
        for i in soup.find_all('div','jet-listing-grid__item'):
                profile_url = i.find('div','jet-engine-listing-overlay-wrap').get('data-url')
                category = i.find('div','elementor-widget-wrap elementor-element-populated').find('h2').text.strip()
                # print(profile_url,':', category)
                details=detailpage(profile_url)

                datas = {
                    'profile_url':profile_url,
                    'category':category
                }
                details.update()
                all_data.append(datas)
                print(datas)
        page_number += 1

all_data = []

listpage()
df = pd.DataFrame(all_data)
df.to_excel('SName.xlsx',index=False)
