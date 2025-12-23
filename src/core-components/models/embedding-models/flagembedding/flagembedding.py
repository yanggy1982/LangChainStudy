# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : flagembedding.py
@time    : 2025/6/6 14:31
@desc    : FlagEmbedding向量模型示例
-----------------------------------------------------------------------
"""
from FlagEmbedding import FlagModel

if __name__ == '__main__':
    print("flagembedding...")
    model = FlagModel('BAAI/bge-base-en-v1.5',
                      query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                      use_fp16=True)

    sentences_1 = ["I love NLP", "I love machine learning"]
    sentences_2 = ["I love BGE", "I love text retrieval"]
    embeddings_1 = model.encode(sentences_1)
    embeddings_2 = model.encode(sentences_2)
    similarity = embeddings_1 @ embeddings_2.T
    print(similarity)