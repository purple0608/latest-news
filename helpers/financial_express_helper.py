from bs4 import BeautifulSoup
import requests
from constant import constant
from response_helper import formatting_response
from request_helper import get_fetch_data
import database

header=constant.FINANCIAL_EXPRESS_HEADER
proxy=constant.PROXY

def financial_express_latestnews():
    data_to_send={}
    
    try:
        #url = constant.LASTEST_ZEE_NEWS_URL
        url=constant.FINANCIAL_EXPRESS_INDIA
        response=get_fetch_data({"url":url,"headers":header})
        #print(response)
        # response = requests.get(url,headers=header,proxies=proxy)
        soup = BeautifulSoup(response, "html.parser")
        latest_news = soup.select('body > div.wp-site-blocks > div.wp-container-11.wp-block-group.margin-top-none > div > div.wp-container-6.wp-block-column.ie-network-grid__lhs')
        content = str(latest_news)
        #print(content)
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
            dict['vendor']='financial express'
            database.save_data_to_db('headlines',dict)
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send
financial_express_latestnews()
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
                dict['link']=i.get('href')
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send


def fetch_data_from_zee_news_url(link):
    try:
        response = requests.get(link,headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        newsData = {}
        heading = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(3) > h1')
        sub_heading = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(4) > h2 > p')
        written_by = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > span:nth-child(1) > a > span')
        edited = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > a > span')
        last_updated = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > span:nth-child(7)')
        print(heading)
        print(sub_heading)
        newsData['heading'] = heading[0].text
        newsData['sub_heading'] = sub_heading[0].text
        newsData['written_by'] = written_by[0].text
        newsData['edited'] = edited[0].text
        newsData['last_updated'] = last_updated[0].text
        print(newsData)
    except Exception as error:
         data_to_send['error']='some thing went wrong'
         print(data_to_send)
    return data_to_send