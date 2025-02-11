import os

import numpy as np
from mongoengine import connect
from sentence_transformers import SentenceTransformer

from app.data.models.document import DocumentModel

# Conecta ao MongoDB
connect(host=os.getenv("MONGO_URI"))

model = SentenceTransformer('all-MiniLM-L6-v2')


def save_document(text: str):
    embedding = model.encode(text).tolist()
    document = DocumentModel(text=text, embedding=embedding)
    document.save()


def search_documents(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()
    documents = DocumentModel.objects()

    results = []
    for doc in documents:
        similarity = np.dot(query_embedding, doc.embedding)
        results.append({"text": doc.text, "similarity": similarity})

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]
