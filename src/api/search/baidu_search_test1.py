# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : baidu_search_test1.py
@time    : 2025/4/16 00:29
@desc    : 
-----------------------------------------------------------------------
"""

from baidusearch.baidusearch import search

if __name__ == '__main__':
    print("baidu_search_test1...")

    # 搜索关键字 "Full Stack Developer"
    results = search('Full Stack Developer')

    # 打印搜索结果
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Abstract: {result['abstract']}")
        print(f"URL: {result['url']}")
        print("-" * 40)
