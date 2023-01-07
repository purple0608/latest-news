from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response

header={

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'traffic_source=https://search.brave.com/; traffic_medium=Referral',
'referer': 'https://zeenews.india.com/latest-news',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'sec-gpc': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'  
}

def Zee_news():
    data_to_send={}
    
    try:
        
        url = constant.LASTEST_ZEE_NEWS_URL
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
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
            dict['headline'] = links[1].text
            for i in links:
                dict['link']=i.get('href')
            list.append(dict)
        data_to_send=formatting_response(True,list,'')
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
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