# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : openai_embeddings.py
@time    : 2025/6/5 16:34
@desc    : OpenAI 向量模型调用示例
-----------------------------------------------------------------------
"""

from langchain_openai import OpenAIEmbeddings

if __name__ == '__main__':
    print("openai_embeddings...")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large",
                                  base_url="https://api.openai-hk.com/v1",
                                  api_key="hk-exj9t51000033960ba84f9d5e6949cad61572f94d42faf93")
    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)
