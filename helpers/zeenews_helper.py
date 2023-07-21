from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response,formatting_responsezb,formatting_responsezs
from helpers.request_helper import get_fetch_data
import helpers.database as database
import asyncio
from requests_html import AsyncHTMLSession
import asyncio
from bs4 import BeautifulSoup
from flask import Flask, render_template
from asyncio import ensure_future

header=constant.ZEE_NEWS_HEADER
proxy=constant.PROXY

async def Zee_news_latestnews():
    data_to_send={}
    
    try:
        url = constant.LASTEST_ZEE_NEWS_URL
        # response = requests.get(url,headers=header)
        # response =  get_fetch_data({"url": url, "headers": header})
        s1 = AsyncHTMLSession()
        response = await s1.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        latest_news = soup.select('body > div.container.catergory-section-container > div > div.col-md-9 > div.row.no-gutters > div.col-lg-5.col-12 > div')
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
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=constant.ZEE_NEWS_ENDPOINT+i.get('href')
                soup = BeautifulSoup(str(i), "html.parser")
                images = soup.select('img')
                # print(images)
                for j in images:
                    dict['image']=j.get('data-original')
            dict['vendor']='zeenews'
            # print(dict)
            database.update_or_create_data('news_headlines',dict,dict)
            list.append(dict)
        # print(list)
        new_list=[]
        data_to_search={'vendor':'zeenews'}
        data=database.get_data_from_db('news_headlines',data_to_search)
        for document in data:
            # print(document)
            new_list.append(document)
        data_to_send=formatting_response(True,new_list,'')
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
    
    # print(data_to_send)
    return data_to_send

# asyncio.run(Zee_news_latestnews())
async def Zee_news_sports():
    data_to_send={}
    try:
        url = constant.SPORTS_ZEE_NEWS_URL
        response = requests.get(url,headers=header)
        response =  get_fetch_data({"url": url, "headers": header, 'proxy': proxy})
        s2 = AsyncHTMLSession()
        response = await s2.get(url)
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
            database.update_or_create_data('news_headlines',dict,dict)
            list.append(dict)
        new_list=[]
        data_to_search={'vendor':'zeenews'}
        data=database.get_data_from_db('news_headlines',data_to_search)
        for document in data:
            # print(document)
            new_list.append(document)
        data_to_send=formatting_responsezs(True,new_list,'')
        # print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
    # print(data_to_send)
    return data_to_send
# h=asyncio.run(Zee_news_sports())

async def Zee_news_buisness():
    data_to_send={}
    try:
        url = constant.BUISNESS_ZEE_NEWS_URL
        response = requests.get(url,headers=header)
        s3 = AsyncHTMLSession()
        response = await (s3.get(url))
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
                database.update_or_create_data('news_headlines',dict,dict)
            list.append(dict)
       
        new_list=[]
        data_to_search={'vendor':'zeenews'}
        data=database.get_data_from_db('news_headlines', data_to_search={'vendor':'zeenews'})
        for document in data:
            # print(document)
            new_list.append(document)
        data_to_send=formatting_response(True,new_list,'')
        # print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_responsezb(False,[],error)
        # print(data_to_send)
    return data_to_send
# Zee_news_buisness()

