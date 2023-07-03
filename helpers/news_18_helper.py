from bs4 import BeautifulSoup
import requests
from constant import constant
from response_helper import formatting_response
from request_helper import get_fetch_data
import database

header=constant.NEWS18_HEADER
proxy=constant.PROXY

def news18_latestnews():
    data_to_send={}
    
    try:
        #url = constant.LASTEST_ZEE_NEWS_URL
        url=constant.NEWS18_URL
        response=get_fetch_data({"url":url,"headers":header})
        #print(response)
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('#__next > div.jsx-3741815684.home_wrapper > div:nth-child(1) > div > div.jsx-3741815684.left_row > div.jsx-679621898.top_story')
        content = str(latest_news)
        #print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            #print(links)
            dict['headline'] = links[0].text
            for i in links:
                dict['link']=i.get('href')
            dict['vendor']='news 18'
            database.save_data_to_db('headlines',dict)
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send
news18_latestnews()
