# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : serp_api_test.py
@time    : 2025/5/7 16:19
@desc    : SerpAPI示例
-----------------------------------------------------------------------
"""

import os
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../env/.env")
serpapi_api_key = os.environ["SERPAPI_API_KEY"]


@tool
def serp_search(query):
    """ 输入搜素关键词，使用SerpAPI调用 """
    params = {
        "engine": "bing",  # 使用Bing搜索引擎
        "gl": "us",  # 设置地理位置为美国
        "hl": "cn",  # 设置语言为英语
    }
    search = SerpAPIWrapper(params=params,serpapi_api_key=serpapi_api_key)
    result = search.run(query)
    return result

if __name__ == '__main__':
    print("serp_api_test...")

    search_term = "熊猫"
    results = serp_search.invoke(search_term)
    print(results)

