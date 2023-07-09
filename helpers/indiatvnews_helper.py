from bs4 import BeautifulSoup
import requests
from helpers.constant import constant
from helpers.response_helper import formatting_response2
from helpers.request_helper import get_fetch_data
import helpers.database as database

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
    #    body > div.wrapper > div.row.two_column.mt10 > div.lhs > div.right_box > div > div.row.latest_hed
        content = str(latest_news)
        #print(content)
        soup = BeautifulSoup(content, "html.parser")
        lines = soup.select('li')
        list = []
        for i in lines:
            dict = {}
            soup = BeautifulSoup(str(i), "html.parser")
            links = soup.select('a')
            # print(links)
            dict['headline'] = links[1].text
            for t in links:
                dict['link']=t.get('href')
                soup = BeautifulSoup(str(t), "html.parser")
                images = soup.select('img')
                # dict['link']=images.get('data-original')
                for j in images:
                    dict['image']=j.get('data-original')
                    

            
               
           
                    
            dict['vendor']='Indiatv news'
        
            # database.save_data_to_db('headlines',dict)
            list.append(dict)
        
        data_to_send=formatting_response2(True,list,'')
    except Exception as  error:
        data_to_send=formatting_response2(False,[],error)
    # print(data_to_send)
    return(data_to_send)
        
# indiatvnews_latestnews()
   

