# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : tavily_extract_test.py
@time    : 2025/12/24 10:19
@desc    : TavilyExtract可以从指定一个或多个URL中提取和分析网页内容
-----------------------------------------------------------------------
"""

import os
from langchain_tavily import TavilyExtract
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../env/.env")
tavily_api_key = os.environ["TAVILY_API_KEY"]

if __name__ == '__main__':
    print("tavily_extract_test...")

    # 初始化提取工具
    extract_tool = TavilyExtract(
        extract_depth="basic",  # 提取深度：basic 或 advanced
        include_images=False,  # 是否包含图片
        tavily_api_key=tavily_api_key
    )

    # 提取网页内容
    result = extract_tool.invoke({"urls": ["https://sports.sina.cn/nba/2019-11-05/detail-iicezuev7034711.d.html"]})
    for i in result:
        print(i, "：", result[i])

