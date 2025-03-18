import json
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from mongoengine import connect, disconnect
from sentence_transformers import SentenceTransformer

load_dotenv()

app = FastAPI(
    title="RAGnostic",
    summary="API para automação de processos internos utilizando RAG (Retrieval-Augmented Generation), processamento de PDFs e IA generativa.",
    description="""
A **RAGnostic** é uma API de automação desenvolvida para o **CSC Banco Bradesco**, que combina técnicas avançadas de **RAG**, processamento de documentos PDF e **IA generativa** para otimizar a extração, armazenamento e recuperação de informações.

## Funcionalidades Principais:
- 📄 **Upload de PDFs**: Extração de texto de documentos PDF, incluindo suporte a OCR para imagens.
- 🗂️ **Armazenamento Flexível**: Armazenamento de documentos no **MongoDB** e/ou em um banco de dados vetorial (**FAISS**) para buscas semânticas.
- 🔍 **Busca Inteligente**: Recuperação de documentos relevantes com base em embeddings e similaridade semântica.
- 🤖 **Geração de Respostas com IA**: Integração com **OpenAI GPT-4** para gerar respostas contextualizadas a partir dos documentos.
- ⚡ **Cache Inteligente**: Utilização do **Redis** para otimizar o desempenho das buscas e respostas.
- 📚 **API Documentada**: Documentação interativa via **Swagger UI** para facilitar a integração e testes.

## Como Utilizar:
1. **Upload de PDFs**: Envie documentos PDF para o endpoint `/documents/upload/` ou `/vector/upload/` para processamento e armazenamento.
2. **Busca de Documentos**: Consulte documentos relevantes usando o endpoint `/search/` (MongoDB) ou `/vector/search/` (FAISS).
3. **Geração de Respostas**: Utilize o endpoint `/ai/generate-answer/` para obter respostas geradas por IA com base nos documentos processados.

Para mais detalhes, acesse a documentação interativa em `/docs`.

```Responsáveis: Danton Issler Rodrigues```
    """,
    version=os.environ.get("VERSION"),
    contact={"name": "Danton Issler Rodrigues", "email": "dantonissler18@gmail.com"},
    openapi_tags=[],
    swagger_ui_parameters={"syntaxHighlight.theme": "ascetic", "deepLinking": False, "defaultModelsExpandDepth": -1, "filter": True, "docExpansion": "none"}
)

# Inicializa o banco de dados mongoengine
host_mongo = os.getenv("MONGO_URI")
disconnect(alias='default')
connect(db='rag_db', host=host_mongo)
model = SentenceTransformer('all-MiniLM-L6-v2')

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

# Caminho para salvar o banco de dados vetorial
VECTOR_STORE_PATH = "resource/vector_store.faiss"

from app.services.vector_service import load_vector_store

# Tenta carregar o banco de dados vetorial existente
vector_store = None
if os.path.exists(VECTOR_STORE_PATH):
    vector_store = load_vector_store()

from app.controllers.document_controller import router as document_router
from app.controllers.search_controller import router as search_router
from app.controllers.vector_controller import router as vector_router
from app.controllers.ai_controller import router as ai_router

# Registra os routers
app.include_router(document_router)
app.include_router(search_router)
app.include_router(vector_router)
app.include_router(ai_router)
