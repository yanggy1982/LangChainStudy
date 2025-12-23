# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : bge_large_zh_v15.py
@time    : 2025/6/5 15:59
@desc    : bge-large-zh-v1.5 向量模型使用示例
-----------------------------------------------------------------------
"""

from langchain_huggingface.embeddings import HuggingFaceEmbeddings

if __name__ == '__main__':
    print("bge_large_zh_v15...")
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceEmbeddings(
        model_name="/Users/yangguangyuan/QuantLib/models/embedding/bge-large-zh-v1.5",
        model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)
    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)
