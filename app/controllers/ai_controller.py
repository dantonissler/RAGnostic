from fastapi import APIRouter, Depends

from app.controllers import get_token, responses  # Função para autenticação
from app.services.rag_service import generate_answer

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/generate-answer/", responses=responses, response_model=dict, status_code=200, description="Gera uma resposta com base em uma consulta textual usando IA.")
async def generate_ai_answer(query: str, token: str = Depends(get_token)):
    # Gera uma resposta usando IA
    answer = generate_answer(query)
    return {"query": query, "answer": answer}
