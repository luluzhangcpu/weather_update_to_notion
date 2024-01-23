

import requests
import time
import argparse
from notion_client import Client
import logging
from datetime import datetime as dt

def get_title(content):
    return {"title": [{"type": "text", "text": {"content": content}}]}

def get_rich_text(content):
    return {"rich_text": [{"type": "text", "text": {"content": content}}]}

def get_date(start):
    return {
        "date": {
            "start": start,
            "time_zone": "Asia/Shanghai",
        }
    }



def insert_to_notion(day1,high,low,weather,date1):
    """插入到notion"""
    time.sleep(0.3)
    parent = {"database_id": database_id, "type": "database_id"}
    properties = {
        "Day":get_title(day1),
        "high":get_rich_text(high),
        "low":get_rich_text(low),
        "weather":get_rich_text(weather),
        "Date":date1
    }
    response = client.pages.create(parent=parent,properties=properties)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("weather_api")
    parser.add_argument("notion_token")
    parser.add_argument("database_id")
    options = parser.parse_args()
    database_id = options.database_id
    notion_token = options.notion_token
    weather_api = options.weather_api
    weather_url = ''.join(['https://api.seniverse.com/v3/weather/daily.json?key=',weather_api,'&location=hangzhou&language=zh-Hans&unit=c&start=0&days=5'])
    a = 1
    while a:
        try:
            file1 = requests.get(weather_url)
        except:
            break
        a = False
    content1 = file1.json()
    results1 = content1.get('results')[0]
    client = Client(auth=notion_token, log_level=logging.ERROR)
    if results1:
        city_forecast1 = results1['daily'][0]  # 当天天气
        city_forecast2 = results1['daily'][1]  # 明天天气
        city_forecast3 = results1['daily'][2]  # 后天天气
        day1 = city_forecast1.get('date')  # 获取当天日期
        date1 = dt.strptime(day1,'%Y-%m-%d')
        high = city_forecast1.get('high') # 获取当天最高温度
        low = city_forecast1.get('low')  # 获取当天最低温度
        weather = city_forecast1.get('text_day') # 获取当天天气类型
        insert_to_notion(day1,high,low,weather,date1)
