# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : real_world_agent.py
@time    : 2025/12/15 10:10
@desc    : 
-----------------------------------------------------------------------
"""

from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv(dotenv_path="../env/.env")

# 定义工具上下文

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# 定义返回报文

@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None

# 定义系统提示词：定义了代理的角色和行为

SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""

# 创建工具：

@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"


if __name__ == '__main__':
    print("real_world_agent...")

    # 定义模型

    model = init_chat_model(
        "claude-sonnet-4-20250514",
        temperature=0.5,
        timeout=10,
        max_tokens=1000
    )

    # 定义检查点

    checkpointer = InMemorySaver()

    agent = create_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_user_location, get_weather_for_location],
        context_schema=Context,
        response_format=ToolStrategy(ResponseFormat),
        checkpointer=checkpointer
    )

    # `thread_id` is a unique identifier for a given conversation.
    config = {"configurable": {"thread_id": "1"}}

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
        config=config,
        context=Context(user_id="1")
    )

    print(response['structured_response'])

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "thank you!"}]},
        config=config,
        context=Context(user_id="1")
    )

    print(response['structured_response'])