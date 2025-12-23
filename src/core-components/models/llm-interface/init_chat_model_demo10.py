# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo10.py
@time    : 2025/12/15 15:53
@desc    :  使用统一模型接口调用模型示例10（工具绑定）
-----------------------------------------------------------------------
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool

load_dotenv(dotenv_path="../../../env/.env")

@tool
def get_weather(location: str) -> str:
    """Get the weather at a location."""
    return f"It's sunny in {location}."


if __name__ == '__main__':
    print("init_chat_model_demo10...")

    model = init_chat_model("gpt-5.1")
    model_with_tools = model.bind_tools([get_weather])

    response = model_with_tools.invoke("What's the weather like in Boston?")
    for tool_call in response.tool_calls:
        # View tool calls made by the model
        print(f"Tool: {tool_call['name']}")
        print(f"Args: {tool_call['args']}")
