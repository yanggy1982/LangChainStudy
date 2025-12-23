# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : flagembedding_rag.py
@time    : 2025/6/6 14:39
@desc    : 基于FlagEmbedding的简易RAG
-----------------------------------------------------------------------
"""

from FlagEmbedding import FlagModel
import faiss
import numpy as np
from openai import OpenAI

if __name__ == '__main__':
    print("flagembedding_rag...")

    # 1、数据准备
    corpus = [
        "Cheli: 一家位于市中心的上海菜餐厅，提供正宗精致的上海风味。人均消费: $40-50",
        "Masa: 位于中城的日本料理，提供由著名厨师Masayoshi Takayama制作的精致寿司和omakase体验。人均消费: $500-600",
        # 其他餐厅信息...
    ]

    user_input = "我想吃中餐"

    # 2、索引构建
    # 2.1、文本嵌入
    # query_instruction_for_retrieval参数为查询添加了特定的指令前缀，这能显著提升检索效果
    # use_fp16=True启用半精度浮点数计算，可以在保持精度的同时提升速度
    model = FlagModel('BAAI/bge-base-en-v1.5',
                      query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                      use_fp16=True)

    embeddings = model.encode(corpus, convert_to_numpy=True)

    # 2.2、向量索引
    index = faiss.IndexFlatIP(embeddings.shape[1]) # IndexFlatIP表示使用内积(Inner Product)作为相似度度量
    index.add(embeddings)

    # 3、检索与生成
    # 3.1、查询处理
    q_embedding = model.encode_queries([user_input], convert_to_numpy=True)

    # 3.2、相似度搜索
    D, I = index.search(q_embedding, 1)
    res = np.array(corpus)[I]

    # 4、生成推荐
    prompt = """
    你是一个餐厅推荐机器人。
    请简洁回答，使用短句不要提供额外信息。
    这些是候选餐厅列表:
    {recommended_activities}
    用户的需求是: {user_input}
    根据用户需求推荐2家餐厅。
    """
    client = OpenAI(base_url="https://api.openai-hk.com/v1",
                    api_key="hk-exj9t51000033960ba84f9d5e6949cad61572f94d42faf93")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个乐于助人的助手。"},
            {
                "role": "user",
                "content": prompt.format(user_input=user_input, recommended_activities=res)
            }
        ]
    )
    print(response)


