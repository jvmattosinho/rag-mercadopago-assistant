from loader import carregar_documentos
from chunker import criar_chunks
from embeddings import adicionar_embeddings
from rag import responder


# 1. Carregar documentos
documentos = carregar_documentos()

# 2. Criar chunks
chunks = criar_chunks(documentos)

# 3. Adicionar embeddings aos chunks
chunks = adicionar_embeddings(chunks)

# 4. Receber a pergunta
pergunta = input("Digite sua pergunta: ")

# 5. Executar o RAG
resposta = responder(
    pergunta,
    chunks
)

# 6. Mostrar resposta
print("\nResposta:")
print(resposta)