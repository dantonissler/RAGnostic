from fastapi import APIRouter, Depends

from app.controllers import get_token, responses
from app.services.document_service import search_documents
from app.services.rag_service import generate_answer

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/generate-answer/", responses=responses, response_model=dict, status_code=200, description="Gera uma resposta baseada na busca de documentos relevantes e na consulta do usuário utilizando IA generativa.", )
async def generate_ai_answer(query: str, token: str = Depends(get_token)):
    documents = search_documents(query, top_k=3)

    if not documents:
        return {"query": query, "answer": "Nenhum documento relevante encontrado."}

    context = "\n\n".join([doc["text"] for doc in documents])
    answer = generate_answer(query, context)

    return {"query": query, "answer": answer, "context": context}