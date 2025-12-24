# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : baidu_search_test2.py
@time    : 2025/4/16 00:32
@desc    : 
-----------------------------------------------------------------------
"""

from baidusearch.baidusearch import search

def get_search_results(keyword, num_results=10):
    results = search(keyword, num_results=num_results)
    return results

if __name__ == '__main__':
    print("baidu_search_test2...")

    # 获取 "Python 教程" 的搜索结果
    python_tutorials = get_search_results('Python 教程', num_results=5)

    for tutorial in python_tutorials:
        #print(f"tutorial: {tutorial}")
        print(f"Title: {tutorial['title']}")
        print(f"URL: {tutorial['url']}")
