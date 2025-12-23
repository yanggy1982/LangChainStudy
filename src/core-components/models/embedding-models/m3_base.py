# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : m3_base.py
@time    : 2025/6/5 16:08
@desc    : m3_base 向量模型使用示例
-----------------------------------------------------------------------
"""
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

if __name__ == '__main__':
    print("m3_base...")

    embeddings = HuggingFaceEmbeddings(model_name="/Users/yangguangyuan/QuantLib/models/embedding/m3e-base")
    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)
