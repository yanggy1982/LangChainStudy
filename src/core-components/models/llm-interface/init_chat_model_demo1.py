# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo1.py
@time    : 2025/12/15 14:07
@desc    : 使用统一模型接口调用模型示例1
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo1...")

    model = init_chat_model("gpt-5.1")
    response = model.invoke("Why do parrots talk?")
    print(response.text)


