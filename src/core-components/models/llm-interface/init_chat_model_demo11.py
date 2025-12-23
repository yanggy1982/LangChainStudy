# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo11.py
@time    : 2025/12/15 17:08
@desc    : 使用统一模型接口调用模型示例11（多模态）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo11...")

    model = init_chat_model("gpt-5.1")
    response = model.invoke("Create a picture of a cat")
    print(response.content_blocks)
