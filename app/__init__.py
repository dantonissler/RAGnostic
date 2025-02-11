import json
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.services.document_service import save_document, search_documents
from app.services.rag_service import generate_answer
from app.utils.pdf_parser import parse_pdf

load_dotenv()

app = FastAPI(
    title="RAGnostic",
    summary="""API para automação de processos internos utilizando RAG, processamento de PDFs e IA generativa.""",
    description="""
    A API de Automação - CSC Banco Bradesco permite o processamento de documentos PDF para extração de informações, 
    armazenamento no MongoDB e recuperação inteligente utilizando embeddings e OpenAI GPT-4.

    ## Funcionalidades:
    - 📄 **Upload de PDFs**: Processamento e extração de texto de documentos.
    - 🔍 **Busca Inteligente**: Localização de documentos relevantes com base em embeddings.
    - 🤖 **Geração de Respostas com IA**: Uso do GPT-4 para fornecer respostas baseadas em contexto.
    - ⚡ **Cache Inteligente**: Utilização do Redis para otimização das buscas.
    - 🔗 **API Documentada**: Acessível via Swagger UI.

    Para mais detalhes, acesse a documentação interativa em `/docs`.
    
```Responsáveis: Danton Issler Rodrigues```
    """,
    version=os.environ.get("VERSION"),
    contact={"name": "Danton Issler Rodrigues", "email": "dantonissler18@gmail.com"},
    openapi_tags=[],
    swagger_ui_parameters={"syntaxHighlight.theme": "ascetic", "deepLinking": False, "defaultModelsExpandDepth": -1, "filter": True, "docExpansion": "none"}
)

from app.utils.files import Files

# Criar a estrutura de pastas necessárias para rodar a aplicação.
Files.create_folder_structure()

try:
    if os.path.exists('logging.json'):
        # Carrega o arquivo de configuração do logging
        with open('logging.json', 'rt') as f:
            config = json.load(f)
        # Configura o logging com base no arquivo de configuração
        logging.config.dictConfig(config)
except Exception as e:
    # Configura o logging com o nível de log INFO como padrão
    logging.basicConfig(level=logging.INFO)

from app.controllers import ai_controller,document_controller

app.include_router(ai_controller.router)
app.include_router(document_controller.router)
