# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : gte_qwen2-7b-instruct.py
@time    : 2025/6/5 16:42
@desc    : gte_qwen2-7b-instruct向量模型调用示例
-----------------------------------------------------------------------
"""
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

if __name__ == '__main__':
    print("gte_qwen2-7b-instruct...")

    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceEmbeddings(
        model_name="/Users/yangguangyuan/QuantLib/models/embedding/gte_Qwen2-7B-instruct",
        model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)

    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)


