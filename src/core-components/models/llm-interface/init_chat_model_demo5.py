# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo5.py
@time    : 2025/12/15 15:25
@desc    : 使用统一模型接口调用模型示例5（流式返回）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo5...")

    model = init_chat_model("gpt-5.1")

    full = None  # None | AIMessageChunk
    for chunk in model.stream("What color is the sky?"):
        full = chunk if full is None else full + chunk
        print(full.text)

    print(full.content_blocks)

