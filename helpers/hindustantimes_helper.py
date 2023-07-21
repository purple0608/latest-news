from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response
from helpers.request_helper import get_fetch_data
import helpers.database as database

header=constant.HINDUSTANTIMES_HEADER
proxy=constant.PROXY

def hindustantimes_latestnews():
    data_to_send={}
    
    try:
        #url = constant.LASTEST_ZEE_NEWS_URL
        url=constant.HINDUSTANTIMES_URL
        response=get_fetch_data({"url":url,"headers":header})
        #print(response)
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('#dataHolder')
        content = str(latest_news)
        #print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('div',{"class":'storyShortDetail'})
        #print(lines)
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.find_all('a')
            if len(links)==0:
                continue
            if links[0]==None:
                continue
            # print(links[0])
            dict['headline'] = links[0].text
            dict['link']=i.get('href')
            list.append(dict)
        new_list=[]
        data=database.get_data_from_db('news_headlines','zeenews')
        for document in data:
            # print(document)
            new_list.append(document)
            # print(links)
        data_to_send=formatting_response(True,new_list,'')
        
        # print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        # print(data_to_send)
    return data_to_send
# hindustantimes_latestnews()
