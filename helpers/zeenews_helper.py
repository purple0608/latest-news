from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response,formatting_responsezb,formatting_responsezs
from helpers.request_helper import get_fetch_data
import helpers.database as database


header=constant.ZEE_NEWS_HEADER
proxy=constant.PROXY

def Zee_news_latestnews():
    data_to_send={}
    
    try:
        url=constant.LASTEST_ZEE_NEWS_URL
        response=get_fetch_data({"url":url,"headers":header,'proxy':proxy})
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select(
            'div.container:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
        content = str(latest_news)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            # print(links)
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=constant.ZEE_NEWS_ENDPOINT+i.get('href')
                soup = BeautifulSoup(str(i), "html.parser")
                images = soup.select('img')
                print(images)
                for j in images:
                    dict['image']=j.get('data-original')
            dict['vendor']='zeenews'
            # database.update_or_create_data('headlines',dict,dict1)
            list.append(dict)
        # print(list)
        data_to_send=formatting_response(True,list,'')
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
    
    print(data_to_send)
    return data_to_send

# Zee_news_latestnews()
def Zee_news_sports():
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
                dict['link']=constant.ZEE_NEWS_ENDPOINT+i.get('href')
            # database.save_data_to_db('headline',dict)
            list.append(dict)
        data_to_send=formatting_responsezs(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send
Zee_news_sports()

def Zee_news_buisness():
    data_to_send={}
    try:
        url = constant.BUISNESS_ZEE_NEWS_URL
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
                dict['link']=constant.ZEE_NEWS_ENDPOINT+i.get('href')
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_responsezb(False,[],error)
        print(data_to_send)
    return data_to_send
Zee_news_buisness()

