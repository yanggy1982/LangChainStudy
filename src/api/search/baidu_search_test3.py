# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : baidu_search_test3.py
@time    : 2025/4/16 00:34
@desc    : 
-----------------------------------------------------------------------
"""

import pandas as pd
from baidusearch.baidusearch import search

if __name__ == '__main__':
    print("baidu_search_test3...")

    # 获取 "数据分析" 的搜索结果
    data_analysis_results = search('数据分析', num_results=20)

    # 将结果转换为 DataFrame
    df = pd.DataFrame(data_analysis_results)

    # 打印前 5 条结果
    print(df.head())