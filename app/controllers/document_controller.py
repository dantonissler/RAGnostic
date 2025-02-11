from fastapi import APIRouter, File, UploadFile, HTTPException, Depends

from app.controllers import responses, get_token
from app.services.document_service import save_document, search_documents
from app.utils.pdf_parser import parse_pdf

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload/", responses=responses, response_model=dict, status_code=201, description="Faz o upload de um arquivo PDF, extrai o texto e armazena no banco de dados para futuras buscas.", )
async def upload_file(file: UploadFile = File(...), token: str = Depends(get_token)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    text = parse_pdf(file.file)
    save_document(text)
    return {"filename": file.filename, "content": text}


@router.get("/search/", responses=responses, response_model=dict, status_code=200, description="Realiza a busca de documentos no banco de dados com base em uma consulta textual.", )
async def search(query: str, token: str = Depends(get_token)):
    documents = search_documents(query, top_k=3)

    if not documents:
        return {"query": query, "answer": "Nenhum documento relevante encontrado."}

    context = "\n\n".join([doc["text"] for doc in documents])
    return {"query": query, "context": context}
