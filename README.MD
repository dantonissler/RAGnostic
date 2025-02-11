# RAGnostic
## API para automação de processos internos utilizando RAG, processamento de PDFs e IA generativa.

## Responsaveis

👨‍💻 **Danton Issler Rodrigues** → 📧 [Contato](mailto:dantonissler18@gmail.com)

## Descricao

Esta API foi desenvolvida para automacao de processos internos utilizando conceitos de **RAG (Retrieval-Augmented Generation)**. Ela permite a extracao, armazenamento e recuperacao de informacoes a partir de documentos PDF, alem de oferecer respostas
baseadas em inteligencia artificial por meio da API da OpenAI.

A solucao combina tecnologias como **FastAPI**, **MongoDB**, **Redis** e **Sentence Transformers**, garantindo uma arquitetura escalavel e eficiente para busca e recuperacao de informacoes.

## Principais Funcionalidades

- **Upload de PDFs**: Processa e armazena o conteudo dos documentos extraindo o texto.
- **Busca de Informacoes**: Utiliza embeddings para localizar documentos relevantes com base em consultas textuais.
- **Geracao de Respostas com IA**: Com base nos documentos encontrados, a API gera respostas otimizadas utilizando **GPT-4**.
- **Cache Inteligente**: Implementacao de cache no Redis para otimizar buscas frequentes e melhorar a performance.
- **Estrutura Modular**: Codigo organizado em servicos distintos, facilitando manutencao e escalabilidade.
- **API Documentada**: Disponível via Swagger UI para facilitar testes e integração.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework Web**: FastAPI
- **Banco de Dados**: MongoDB
- **Armazenamento de Cache**: Redis
- **Processamento de PDFs**: PyMuPDF
- **Modelo de Embeddings**: Sentence Transformers
- **Integracao com IA**: OpenAI GPT-4

## Arquitetura do Projeto

A API segue uma arquitetura **orientada a servicos**, onde cada funcionalidade principal e tratada por um modulo independente, incluindo:

- **document\_service.py** → Responsavel por armazenar e recuperar documentos usando embeddings.
- **rag\_service.py** → Gera respostas com IA usando contexto extraido dos documentos.
- **cache\_service.py** → Gerencia o cache para otimizar a performance.
- **pdf\_parser.py** → Realiza a extracao de texto de arquivos PDF.
- **files.py** → Gerencia operações com arquivos, incluindo conversão para base64.

## Implantacao

O projeto pode ser facilmente implantado usando **Docker e Docker Compose**, garantindo um ambiente padronizado e replicavel.

### Como Executar

1. **Clone o repositorio**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_PROJETO>
   ```
2. **Instale as dependencias**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure as variaveis de ambiente** (arquivo `.env`)
4. **Suba os servicos com Docker**:
   ```bash
   docker-compose up -d
   ```
5. **Acesse a API via Swagger UI**:
   ```
   http://localhost:8000/docs
   ```
