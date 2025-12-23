# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo3.py
@time    : 2025/12/15 14:48
@desc    : 使用统一模型接口调用模型示例3（包含消息对象列表的历史记录）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv(dotenv_path="../../../env/.env")

conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]

if __name__ == '__main__':
    print("init_chat_model_demo3...")

    model = init_chat_model("gpt-5.1")
    response = model.invoke(conversation)
    print(response)
