# app/memory/vector_store.py
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

db = None

def store(text):
    global db
    if db is None:
        db = FAISS.from_texts([text], embeddings)
    else:
        db.add_texts([text])

def retrieve(query):
    if db is None:
        return []
    return db.similarity_search(query)