# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : ollama_embeddings.py
@time    : 2025/6/5 16:11
@desc    : ollama 向量模型调用示例
-----------------------------------------------------------------------
"""

from langchain_ollama import OllamaEmbeddings

if __name__ == '__main__':
    print("ollama_embeddings...")
    embeddings = OllamaEmbeddings(model="llama3.2")
    # embeddings = OllamaEmbeddings(model="herald/dmeta-embedding-zh")
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")

    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)
