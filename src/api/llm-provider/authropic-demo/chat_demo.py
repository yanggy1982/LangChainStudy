# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : chat_demo.py
@time    : 2025/12/23 09:44
@desc    : cladu的api测试
-----------------------------------------------------------------------
"""
import os

import anthropic
import httpx
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../../env/.env")
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if __name__ == '__main__':
    print("chat_demo...")

    BASE_URL = "https://sg.uiuiapi.com"
    # MODEL_NAME = "claude-sonnet-4-20250514"
    MODEL_NAME = "claude-opus-4-5-20251101"

    try:
        # 初始化客户端
        client_params = {
            "api_key": API_KEY,
            "base_url": BASE_URL,
            "timeout": httpx.Timeout(300.0, connect=60.0),  # 总体超时300秒，连接阶段超时60秒
            "max_retries": 1,
        }

        client = anthropic.Anthropic(**client_params)

    except Exception as e:
        print(f"创建 Anthropic 客户端时发生错误: {e}")
        exit()

    messages_payload = [
        {"role": "user", "content": "你好，你能做什么？请用中文回答。"}
    ]

    # 4. 发送请求并处理响应
    try:
        print(f"\n正在尝试调用 Anthropic API (模型: {MODEL_NAME})...")
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=200,  # 建议至少150-200 tokens for Claude 3 Sonnet for meaningful replies
            temperature=0.7,  # 温度参数，控制生成文本的随机性
            messages=messages_payload,
            system="You are a helpful assistant."  # 可选的系统提示
        )

        # 5. 提取并打印模型生成的回复内容
        if response.content and isinstance(response.content, list) and len(response.content) > 0:
            # 通常，对于非流式响应，内容在 response.content[0].text
            assistant_reply = response.content[0].text
            print("\n模型回复:")
            print(assistant_reply)
        else:
            print("\n未能从 API 获取有效回复。")
            if response.stop_reason:
                print(f"停止原因: {response.stop_reason}")
            # print("完整响应对象:", response.model_dump_json(indent=2)) # 用于调试

        # 打印用量信息（如果可用）
        if response.usage:
            print("\n用量信息:")
            print(f"  输入 Token: {response.usage.input_tokens}")
            print(f"  输出 Token: {response.usage.output_tokens}")

    except anthropic.APIStatusError as e:
        print(f"\nAnthropic API 返回了错误状态码: {e.status_code}")
        print(f"错误类型: {e.type}" if hasattr(e, 'type') and e.type else "")
        print(f"错误消息: {e.message}" if hasattr(e, 'message') and e.message else "")
        print(f"响应详情: {e.response}")  # 包含原始的 httpx.Response
        if e.status_code == 401:
            print("错误详情：API 密钥无效或未提供。请检查您的 ANTHROPIC_API_KEY。")
        elif e.status_code == 403:
            print("错误详情：认证成功，但密钥无权访问所请求的资源/模型，或已超出使用限制，或账户存在问题。")
            print(f"  - 请检查您的 Anthropic 账户是否有权访问模型 '{MODEL_NAME}'。")
            print("  - 检查您的账户用量、账单状态和 API 密钥权限。")
            print("  - 尝试使用其他模型，例如 'claude-3-haiku-20240307' 或 'claude-3-sonnet-20240229'。")
        elif e.status_code == 404:
            print(f"错误详情：找不到请求的资源。很可能是模型名称 '{MODEL_NAME}' 不正确或不可用。")
            print("  - 请检查 Anthropic 文档以获取正确的模型名称。")
        elif e.status_code == 429:
            print("错误详情：达到 Anthropic API 速率限制。请稍后重试或检查您的速率限制策略。")
        elif e.status_code >= 500:
            print("错误详情：Anthropic 服务器端错误。请稍后重试。")
    except anthropic.APIConnectionError as e:
        print(f"\n无法连接到 Anthropic API: {e}")
        print("  - 请检查您的网络连接。")
        print(f"  - 如果您使用了自定义 Base URL ('{BASE_URL}'), 请确保它正确且可访问。")
    except anthropic.RateLimitError as e:
        print(f"\n达到 Anthropic API 速率限制: {e}")
    except anthropic.AuthenticationError as e:
        print(f"\nAnthropic API 认证失败: {e}")
        print("  - 请再次检查您的 ANTHROPIC_API_KEY 是否正确且有效。")
    except Exception as e:
        print(f"\n调用 API 时发生未知错误: {e}")
        print(f"错误类型: {type(e).__name__}")