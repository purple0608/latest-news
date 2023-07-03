from bs4 import BeautifulSoup
import requests
from constant import constant
from response_helper import formatting_response
from request_helper import get_fetch_data
import database

header=constant.INDIATVNEWS_HEADER
proxy=constant.PROXY

def indiatvnews_latestnews():
    data_to_send={}
    
    try:
        #url = constant.LASTEST_ZEE_NEWS_URL
        url=constant.INDIATVNEWS_URL
        response=get_fetch_data({"url":url,"headers":header})
        #print(response)
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('body > div.wrapper > div.row.two_column.election-result > div.rhs.mt35')
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
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=i.get('href')
            dict['vendor']='Indiatv news'
            database.save_data_to_db('headlines',dict)
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send
indiatvnews_latestnews()
