from flask import Flask
from bs4 import BeautifulSoup
import requests
from flask import render_template
from helpers import zeenews_helper
from helpers import economic_news_helper
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello world'
@app.route('/zee')
def Zee_news():
    news_data= zeenews_helper.Zee_news()
    print(news_data)
    return news_data


@app.route('/economics')
def economics_times():
    news_data= economic_news_helper.Economictimes_news()
    print(news_data)
    return news_data
    
if __name__ == '__main__':
    app.run()
