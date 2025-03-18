from fastapi import APIRouter, File, UploadFile, HTTPException, Depends

from app.controllers import get_token, responses
from app.services.vector_service import create_vector_store, search_vector_store
from app.utils.pdf_parser import parse_pdf

router = APIRouter(prefix="/vector", tags=["Vector"])


@router.post("/upload/", responses=responses, response_model=dict, status_code=201, description="Faz o upload de um arquivo PDF, extrai o texto e armazena no banco vetorial (FAISS).")
async def upload_file(file: UploadFile = File(...), token: str = Depends(get_token)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    # Extrai o texto do PDF
    text = parse_pdf(file.file)

    # Cria e salva o banco de dados vetorial
    create_vector_store(text)
    return {"filename": file.filename, "message": "PDF processed and stored in vector database"}


@router.get("/search/", responses=responses, response_model=dict, status_code=200, description="Realiza a busca de documentos no banco vetorial (FAISS) com base em uma consulta textual.")
async def search(query: str, token: str = Depends(get_token)):
    # Busca documentos relevantes no banco vetorial
    results = search_vector_store(query)
    return {"query": query, "results": results}
