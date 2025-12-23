# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo4.py
@time    : 2025/12/15 15:19
@desc    : 使用统一模型接口调用模型示例4（流式返回）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo4...")

    model = init_chat_model("gpt-5.1")
    for chunk in model.stream("Why do parrots have colorful feathers?"):
        print(chunk.text, end="|", flush=True)


