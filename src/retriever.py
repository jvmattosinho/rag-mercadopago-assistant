import math

from embeddings import gerar_embedding


def similaridade_cosseno(vetor_a, vetor_b):

    produto = sum(
        a * b
        for a, b in zip(vetor_a, vetor_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vetor_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vetor_b)
    )

    return produto / (magnitude_a * magnitude_b)


def buscar_chunks(pergunta, chunks, top_k=3):

    # Gera o embedding da pergunta
    embedding_pergunta = gerar_embedding(pergunta)

    # Compara a pergunta com cada chunk
    for chunk in chunks:
        chunk["similaridade"] = similaridade_cosseno(
            embedding_pergunta,
            chunk["embedding"]
        )

    # Ordena do mais parecido para o menos parecido
    chunks_ordenados = sorted(
        chunks,
        key=lambda chunk: chunk["similaridade"],
        reverse=True
    )

    # Retorna somente os mais relevantes
    return chunks_ordenados[:top_k]