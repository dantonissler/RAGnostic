from fastapi import APIRouter, File, UploadFile, HTTPException, Depends

from app.controllers import get_token, responses  # Função para autenticação
from app.services.document_service import save_document
from app.utils.pdf_parser import parse_pdf

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload/", responses=responses, response_model=dict, status_code=201, description="Faz o upload de um arquivo PDF, extrai o texto e armazena no MongoDB.")
async def upload_file(file: UploadFile = File(...), token: str = Depends(get_token)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    # Extrai o texto do PDF
    text = parse_pdf(file.file)

    # Salva o documento no MongoDB
    save_document(text)

    return {"filename": file.filename, "content": text}
