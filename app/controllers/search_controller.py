from fastapi import APIRouter, Depends

from app.controllers import get_token, responses
from app.services.document_service import search_documents
from app.services.rag_service import generate_answer

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/", responses=responses, response_model=dict, status_code=200, description="Realiza a busca de documentos no MongoDB com base em uma consulta textual.")
async def search(query: str, token: str = Depends(get_token)):
    # Busca os documentos mais relevantes
    documents = search_documents(query, top_k=3)

    if not documents:
        return {"query": query, "answer": "Nenhum documento relevante encontrado."}

    # Concatena os textos dos documentos mais relevantes para formar o contexto
    context = "\n\n".join([doc["text"] for doc in documents])

    # Gera a resposta usando OpenAI
    answer = generate_answer(query, context)

    return {"query": query, "answer": answer, "context": context, "model": "OpenAI GPT-4"}
