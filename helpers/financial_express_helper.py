from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response1
from helpers.request_helper import get_fetch_data
import helpers.database as database

header=constant.FINANCIAL_EXPRESS_HEADER
proxy=constant.PROXY

def financial_express_latestnews():
    data_to_send={}
    
    try:
        #url = constant.LASTEST_ZEE_NEWS_URL
        url=constant.FINANCIAL_EXPRESS_INDIA
        response=get_fetch_data({"url":url,"headers":header})
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('body > div.wp-site-blocks > div.wp-container-12.wp-block-group.margin-top-none > div > div.wp-container-10.wp-block-column.ie-network-grid__rhs > div.wp-block-template-part')
        content = str(latest_news)
        # print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('article')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=i.get('href')
                soup = BeautifulSoup(str(i), "html.parser")
                images = soup.select('img')
                # print(images)
                # dict['link']=images.get('data-original')
                for j in images:
                    dict['image']=j.get('src')
            dict['vendor']='financial express'
            # database.save_data_to_db('headlines',dict)
            list.append(dict)
        data_to_send=formatting_response1(True,list,'')
        # print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response1(False,[],error)
        # print(data_to_send)
    return data_to_send

def financial_express_sports():
    data_to_send={}
    try:
        url = constant.SPORTS_ZEE_NEWS_URL
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        sports_news = soup.select('body > div.container.catergory-section-container > div > div.col-md-9 > div.row.no-gutters > div.col-lg-5.col-12')
        content = str(sports_news)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=i.get('href')
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send

