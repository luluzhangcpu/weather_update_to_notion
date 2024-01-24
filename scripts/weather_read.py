

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
        }
    }



def insert_to_notion(day1,high,low,weather_day,weather_night,rainfall,precipitation,\
                     wind_direction,wind_direction_degree,wind_speed,wind_scale,humidity):
    """插入到notion"""
    time.sleep(0.3)
    parent = {"database_id": database_id, "type": "database_id"}
    properties = {
        "Day":get_title(day1),
        "high":get_rich_text(high),
        "low":get_rich_text(low),
        "weather_day":get_rich_text(weather_day),
        "weather_night":get_rich_text(weather_night),
        "rainfall":get_rich_text(rainfall),
        "precipitation":get_rich_text(precipitation),
        "wind_direction":get_rich_text(wind_direction),
        "wind_direction_degree":get_rich_text(wind_direction_degree),
        "wind_speed":get_rich_text(wind_speed),
        "wind_scale":get_rich_text(wind_scale),
        "humidity":get_rich_text(humidity),
        "Date":get_date(day1)
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
        high = city_forecast1.get('high') # 获取当天最高温度
        low = city_forecast1.get('low')  # 获取当天最低温度
        weather_day = city_forecast1.get('text_day') # 获取白天天气类型
        weather_night = city_forecast1.get('text_night') # 获取晚上天气类型
        rainfall = city_forecast1.get('rainfall') # 获取晚上天气类型
        precipitation = city_forecast1.get('precip') # 获取晚上天气类型
        wind_direction = city_forecast1.get('wind_direction')
        wind_direction_degree = city_forecast1.get('wind_direction_degree')
        wind_speed = city_forecast1.get('wind_speed')
        wind_scale = city_forecast1.get('wind_scale')
        humidity = city_forecast1.get('humidity')       
        insert_to_notion(day1,high,low,weather_day,weather_night,rainfall,precipitation,\
                         wind_directrion,wind_direction_degree,wind_speed,wind_scale,humidity)
