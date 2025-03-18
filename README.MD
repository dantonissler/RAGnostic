# RAGnostic

## API para automação de processos internos utilizando RAG, processamento de PDFs e IA generativa.

**RAGnostic** é uma API de automação desenvolvida para o **CSC Banco Bradesco**, que combina técnicas avançadas de **RAG (Retrieval-Augmented Generation)**, processamento de documentos PDF e **IA generativa** para otimizar a extração, armazenamento e
recuperação de informações.

## Responsaveis

👨‍💻 **Danton Issler Rodrigues** → 📧 [Contato](mailto:dantonissler18@gmail.com)

---

## Funcionalidades Principais

- 📄 **Upload de PDFs**: Extração de texto de documentos PDF, incluindo suporte a OCR para imagens.
- 🗂️ **Armazenamento Flexível**: Armazenamento de documentos no **MongoDB** e/ou em um banco de dados vetorial (**FAISS**) para buscas semânticas.
- 🔍 **Busca Inteligente**: Recuperação de documentos relevantes com base em embeddings e similaridade semântica.
- 🤖 **Geração de Respostas com IA**: Integração com **OpenAI GPT-4** para gerar respostas contextualizadas a partir dos documentos.
- ⚡ **Cache Inteligente**: Utilização do **Redis** para otimizar o desempenho das buscas e respostas.
- 📚 **API Documentada**: Documentação interativa via **Swagger UI** para facilitar a integração e testes.

---

## Como Utilizar

### Endpoints Principais

1. **Upload de PDFs**:
    - **Endpoint**: `POST /documents/upload/` (MongoDB) ou `POST /vector/upload/` (FAISS).
    - **Descrição**: Envie documentos PDF para processamento e armazenamento.
    - **Exemplo**:
      ```bash
      curl -X POST "http://localhost:8000/documents/upload/" -H "Content-Type: multipart/form-data" -F "file=@/caminho/para/seu/arquivo.pdf"
      ```

2. **Busca de Documentos**:
    - **Endpoint**: `GET /search/` (MongoDB) ou `GET /vector/search/` (FAISS).
    - **Descrição**: Consulte documentos relevantes com base em uma consulta textual.
    - **Exemplo**:
      ```bash
      curl -X GET "http://localhost:8000/search/?query=Qual%20é%20o%20tema%20principal%20do%20documento?"
      ```

3. **Geração de Respostas com IA**:
    - **Endpoint**: `GET /ai/generate-answer/`.
    - **Descrição**: Gere respostas contextualizadas usando OpenAI GPT-4.
    - **Exemplo**:
      ```bash
      curl -X GET "http://localhost:8000/ai/generate-answer/?query=Explique%20o%20que%20é%20machine%20learning."
      ```

---

## Instalação

### Pré-requisitos

- **Docker** e **Docker Compose** instalados.
- **OpenAI API Key** (disponível em [OpenAI](https://platform.openai.com/)).

### Passos para Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ragnostic.git
   cd ragnostic
   ```

2. Crie um arquivo `.env` na raiz do projeto e adicione suas variáveis de ambiente:
   ```plaintext
   OPENAI_API_KEY=sua_chave_openai
   MONGO_URI=mongodb://mongo:27017/rag_db
   REDIS_URL=redis://redis:6379
   ```

3. Construa e execute os contêineres Docker:
   ```bash
   docker-compose up --build
   ```

4. Acesse a API em `http://localhost:8000`.

---

## Estrutura do Projeto

```
RAGnostic/
│
├── app/
│   ├── __init__.py
│   ├── controllers/                  # Pasta para os controllers
│   │   ├── __init__.py
│   │   ├── document_controller.py    # Controller para upload de documentos (MongoDB)
│   │   ├── search_controller.py      # Controller para busca de documentos (MongoDB)
│   │   ├── vector_controller.py      # Controller para operações com o banco vetorial (FAISS)
│   │   └── ai_controller.py          # Controller para geração de respostas com IA
│   ├── models/
│   │   └── document.py               # Modelo do MongoDB para documentos
│   ├── services/
│   │   ├── document_service.py       # Serviço para operações com documentos (MongoDB)
│   │   ├── vector_service.py         # Serviço para operações com o banco vetorial (FAISS)
│   │   ├── rag_service.py            # Serviço para geração de respostas com IA
│   │   └── cache_service.py          # Serviço para cache com Redis
│   └── utils/
│       ├── pdf_parser.py             # Utilitário para extrair texto de PDFs
│       └── files.py                  # Utilitário para manipulação de arquivos
│
├── requirements.txt
├── logging.json
├── Dockerfile
└── docker-compose.yml
├── requirements.txt
```

---

## Documentação da API

Acesse a documentação interativa da API em `http://localhost:8000/docs`.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção da API.
- **MongoDB**: Banco de dados para armazenamento de documentos.
- **FAISS**: Banco de dados vetorial para buscas semânticas.
- **OpenAI GPT-4**: Modelo de IA para geração de respostas.
- **Redis**: Cache para otimização de buscas.
- **Docker**: Contêinerização e orquestração de serviços.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

- **Responsável**: Danton Issler Rodrigues
- **Email**: dantonissler18@gmail.com

---

Com esse **README.md**, seu projeto estará bem documentado e fácil de entender para colaboradores e usuários. Se precisar de mais ajustes, é só avisar! 🚀