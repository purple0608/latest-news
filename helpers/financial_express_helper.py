from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response

header={

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9', 
'cookie': 'geoinfo=CC:IN, RC:AP, CT:VIJAYAWADA, CO:AS, GL:1; _hookShow=1; fpid=e6fa72b2ee247adafaca00381f2799c41672659246; pfuuid=1644912066746711; popout_autorefresh_open=true; rw_default=true; g_state={"i_p":1673011398744,"i_l":2}; et_interstitial_active=true; int_fcapcount=2',
'referer': 'https://economictimes.indiatimes.com/defaultinterstitial.cms',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-gpc': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def Economictimes_news():
    data_to_send={}
    try:
        url = constant.LASTEST_ECONOMIC_NEWS_URL
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        latest_news = soup.select('#topNewsTabs > div.tabsContent.clearfix > ul')
        content = str(latest_news)
        print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            print(i.text)
        # for i in lines:
        #     dict = {}
        #     soup = BeautifulSoup(str(i), "html.parser")
        #     links = soup.select('li')
        #     print(links)
        #     dict['headline'] = links[1].text
        #     # for i in links:
        #     #     dict['link']=i.get('href')
        #     list.append(dict)
        # data_to_send=formatting_response(True,list,'')
        print(data_to_send)
    except Exception as  error:
        data_to_send=formatting_response(False,[],error)
        print(data_to_send)
    return data_to_send
Economictimes_news()
# def fetch_data_from_economicstimes_news_url(link):
#     response = requests.get(link,headers=header)
#     soup = BeautifulSoup(response.content, "html.parser")
#     newsData = {}
#     heading = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(3) > h1')
#     sub_heading = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(4) > h2 > p')
#     written_by = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > span:nth-child(1) > a > span')
#     edited = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > a > span')
#     last_updated = soup.select('body > section.main-container.articledetails-page > div.container > div > div.col-12.col-md-9.pl-0 > div:nth-child(5) > div > span:nth-child(7)')
#     print(heading)
#     print(sub_heading)
#     newsData['heading'] = heading[0].text
#     newsData['sub_heading'] = sub_heading[0].text
#     newsData['written_by'] = written_by[0].text
#     newsData['edited'] = edited[0].text
#     newsData['last_updated'] = last_updated[0].text
#     print(newsData)
# fetch_data_from_economicstimes_news_url()