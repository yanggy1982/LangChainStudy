# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo9.py
@time    : 2025/12/15 15:44
@desc    : 使用统一模型接口调用模型示例9（批量处理，控制同时处理的并发）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo9...")

    model = init_chat_model("gpt-5.1")
    responses = model.batch(
        [
        "Why do parrots have colorful feathers?",
        "How do airplanes fly?",
        "What is quantum computing?"
        ],
        config={'max_concurrency': 5,}
    )
    for response in responses:
        print(response)
