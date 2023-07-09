import requests
from helpers.constant import constant
def get_fetch_data(params,proxy=False):
    proxies= {'http': 'http://3.111.55.27:80','https': 'http://3.111.55.27:80'}
    if not proxy:
        proxies={}
    url=params.get("url")
    headers=params.get("headers") if params.get("headers")!=None else {}
    cookies= params.get("cookie") if params.get("cookie")!=None else {}
    response = requests.get(url,headers=headers,cookies=cookies,proxies=proxies)
    return response.content
     


