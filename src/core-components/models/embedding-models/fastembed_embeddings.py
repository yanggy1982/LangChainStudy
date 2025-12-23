# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : fastembed_embeddings.py
@time    : 2025/6/5 16:54
@desc    : 
-----------------------------------------------------------------------
"""

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

if __name__ == '__main__':
    print("fastembed_embeddings...")

    embeddings = FastEmbedEmbeddings(cache_dir="/Users/yangguangyuan/QuantLib/models/fastembed")
    #embeddings = FastEmbedEmbeddings(cache_dir="/Users/yangguangyuan/platform/AiLab/models/fastembed",api_base="http://api.wlai.vip")

    text = "This is a test document."
    doc_result = embeddings.embed_documents([text])
    print(doc_result)
