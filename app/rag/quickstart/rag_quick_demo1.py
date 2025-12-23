# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : rag_quick_demo1.py
@time    : 2025/12/23 15:39
@desc    : RAG示例1
-----------------------------------------------------------------------
"""

from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

if __name__ == '__main__':
    print("rag_quick_demo1...")

    # 1、读取文本信息
    loader = TextLoader("/Users/yangguangyuan/QuantLib/docs/观潮.txt", encoding='utf-8')
    documents = loader.load()

    # 2、文本分割
    text_splitter = CharacterTextSplitter(chunk_size=128, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)

    #for document in documents:
    #    print(document)

    # 向量化 embedding model: m3e-base
    embedding = HuggingFaceEmbeddings(
        model_name="/Users/yangguangyuan/QuantLib/models/embedding/bge-large-zh-v1.5")
    db = Chroma.from_documents(documents, embedding)
    retriever = db.as_retriever()

    llm = ChatOllama(model="qwen3:32b", temperature=0.8)

    template = """ 
                Answer the question based only on the following context: {context} Question: {question} 
                """

    prompt = ChatPromptTemplate.from_template(template)

    chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())

    resp = chain.invoke("什么时间去哪里观潮比较合适？")
    print(resp)

