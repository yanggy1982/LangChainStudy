# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : basic_agent_demo2.py
@time    : 2025/12/12 00:27
@desc    : 基本智能体示例2
-----------------------------------------------------------------------
"""

from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv(dotenv_path="../env/.env")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

if __name__ == '__main__':
    print("basic_agent_demo2...")

    agent = create_agent(
        model="claude-sonnet-4-20250514",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    inputs = {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    for chunk in agent.stream(inputs, stream_mode="updates"):
        print(chunk)
