# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : init_chat_model_demo6.py
@time    : 2025/12/15 15:31
@desc    : 使用统一模型接口调用模型示例6（流式返回）
-----------------------------------------------------------------------
"""
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(dotenv_path="../../../env/.env")

async def main():
    model = init_chat_model("gpt-5.1")
    async for event in model.astream_events("Hello"):

        if event["event"] == "on_chat_model_start":
            print(f"Input: {event['data']['input']}")

        elif event["event"] == "on_chat_model_stream":
            print(f"Token: {event['data']['chunk'].text}")

        elif event["event"] == "on_chat_model_end":
            print(f"Full message: {event['data']['output'].text}")

        else:
            pass

if __name__ == '__main__':
    print("init_chat_model_demo6...")
    asyncio.run(main())


