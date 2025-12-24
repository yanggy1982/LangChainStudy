# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : seniverse_api_test.py
@time    : 2025/5/7 14:16
@desc    : 通过Seniverse天气API获取天气
-----------------------------------------------------------------------
"""
import requests
from langchain_core.tools import tool
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../env/.env")
seniverse_api_key = os.environ["SENIVERSE_API_KEY"]

@tool
def get_weather(location:str):
    """ 根据城市获取天气数据 """
    url = f'https://api.seniverse.com/v3/weather/now.json?key={seniverse_api_key}&location={location}&language=zh-Hans&unit=c'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["results"]
        print(f"data={data}")
        name = data[0]["location"]['name']
        temperature = data[0]['now']["temperature"]
        text = data[0]['now']["text"]
        return name+"，当前天气："+text+"，温度："+temperature+ "℃"
    else:
        raise Exception(f"获取天天信息失败：{response.status_code}")

if __name__ == '__main__':
    print("seniverse_api_test...")
    result = get_weather.invoke("哈尔滨")
    print(f"result:{result}")
