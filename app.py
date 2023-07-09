from flask import Flask
from bs4 import BeautifulSoup
import requests
from flask import render_template
from bson import ObjectId
import json
from bson import ObjectId
from flask import Flask, Response
from flask import Flask, redirect, url_for

from helpers import indiatvnews_helper
from helpers import news_18_helper
from helpers import financial_express_helper
from helpers import zeenews_helper
from helpers import hindustantimes_helper
def convert_objectid_to_string(data):
    if isinstance(data, dict):
        return {k: convert_objectid_to_string(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_objectid_to_string(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data

app = Flask(__name__)


@app.route('/index')
def index():
    news_data1 =financial_express_helper.financial_express_latestnews()
    news_data2 = news_18_helper.news18_latestnews()
    news_data3 = indiatvnews_helper.indiatvnews_latestnews()
    zee_news_latest=zeenews_helper.Zee_news_latestnews()
    
    return render_template('index.html',data1=news_data1,data2=news_data2,data3=news_data3,data4=zee_news_latest)

@app.route('/gallery')
def gallery():
    return render_template('index.html')

@app.route('/full_width')
def full_width():
    return render_template('index.html')

@app.route('/sidebar_left')
def sidebar_left():
    return render_template('index.html')

@app.route('/sidebar_right')
def sidebar_right():
    return render_template('index.html')

@app.route('/basic_grid')
def basic_grid():
    return render_template('index.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/latest')
def latest():
    news_data1 =financial_express_helper.financial_express_latestnews()
    news_data2 = news_18_helper.news18_latestnews()
    news_data3 = indiatvnews_helper.indiatvnews_latestnews()
   
    
    return render_template('latest.html',data1=news_data1,data2=news_data2,data3=news_data3)

@app.route('/latest_sports')
def latest_sports():
    news_datazs =zeenews_helper.Zee_news_sports()
    return render_template('sports_news.html',datazs=news_datazs)



    
if __name__ == '__main__':
    app.run()
