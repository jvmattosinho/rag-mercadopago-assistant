# RAG Mercado Pago Assistant

Projeto desenvolvido para estudo prático de **RAG (Retrieval-Augmented Generation)** utilizando Python e OpenAI.

A aplicação utiliza uma base local de documentos sobre o Mercado Pago para buscar informações relevantes e utilizá-las como contexto para um LLM responder perguntas.

## Como funciona

O fluxo do RAG implementado é:

```text
Documentos
    ↓
Chunking
    ↓
Embeddings
    ↓
Retrieval
    ↓
Top-K
    ↓
Contexto
    ↓
LLM
    ↓
Resposta
```

## Estrutura do projeto

```text
rag-mercadopago-assistant/
├── data/
│   └── documents/
│       ├── autenticacao.md
│       └── pagamentos.md
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── rag.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Tecnologias

- Python
- OpenAI API
- Embeddings
- Similaridade de cosseno
- Retrieval-Augmented Generation (RAG)

## Executando o projeto

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Execute a aplicação:

```bash
python src/main.py
```

## Exemplo

Pergunta:

```text
Como evitar criar o mesmo pagamento duas vezes?
```

Resposta:

```text
Use o header X-Idempotency-Key na criação da order para evitar
a criação duplicada quando a mesma solicitação for repetida.
```

## Objetivo

O objetivo deste projeto é compreender na prática cada etapa de um RAG, implementando manualmente o processo de carregamento de documentos, chunking, geração de embeddings, busca por similaridade e geração da resposta com um LLM.