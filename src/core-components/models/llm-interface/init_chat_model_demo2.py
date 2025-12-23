# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo2.py
@time    : 2025/12/15 14:33
@desc    : 使用统一模型接口调用模型示例2（包含字典形式的历史记录）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

if __name__ == '__main__':
    print("init_chat_model_demo2...")

    conversation = [
        {"role": "system", "content": "You are a helpful assistant that translates English to French."},
        {"role": "user", "content": "Translate: I love programming."},
        {"role": "assistant", "content": "J'adore la programmation."},
        {"role": "user", "content": "Translate: I love building applications."}
    ]

    model = init_chat_model("gpt-5.1")
    response = model.invoke(conversation)
    print(response)
