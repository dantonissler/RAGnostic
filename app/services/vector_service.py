import os

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from app import VECTOR_STORE_PATH


def create_vector_store(chunks):
    """
    Cria um banco de dados vetorial com os chunks de texto.
    """
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store


def search_vector_store(query: str):
    """
    Busca documentos relevantes no banco de dados vetorial.
    """
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vector_store = FAISS.load_local("/data/vector_store.faiss", embeddings, allow_dangerous_deserialization=True)
    results = vector_store.similarity_search(query, k=3)
    return [doc.page_content for doc in results]


def save_vector_store(vector_store):
    """
    Salva o banco de dados vetorial em um arquivo.
    """
    vector_store.save_local(VECTOR_STORE_PATH)


def load_vector_store():
    """
    Carrega o banco de dados vetorial de um arquivo.
    """
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True  # Permite a desserialização de arquivos pickle
    )
    return vector_store
