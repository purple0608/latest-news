from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response3
from helpers.request_helper import get_fetch_data
import helpers.database as database

header=constant.NEWS18_HEADER
proxy=constant.PROXY

def news18_latestnews():
    data_to_send={}
    
    try:
       
        url=constant.NEWS18_URL
        response=get_fetch_data({"url":url,"headers":header})
        #print(response)
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('#__next > div.jsx-3741815684.home_wrapper > div:nth-child(1) > div > div.right_row > div:nth-child(9)')
        content = str(latest_news)
        # print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            # print(links)
            dict['headline'] = links[0].text
            for i in links:
                dict['link']=i.get('href')
                soup = BeautifulSoup(str(i), "html.parser")
                images = soup.select('img')
                # print(images)
                for j in images:
                    dict['image']=j.get('src')
            dict['vendor']='news 18'
            database.update_or_create_data('news_headlines',dict,dict)
            list.append(dict)
        new_list=[]
        data_to_search={'vendor':'news 18'}
        data=database.get_data_from_db('news_headlines',data_to_search)
        for document in data:
            # print(document)
            new_list.append(document)
        # print(list)
        data_to_send=formatting_response3(True,new_list,'')
        # print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response3(False,[],error)
        # print(data_to_send)
    # print(data_to_send)
    return data_to_send

# news18_latestnews()