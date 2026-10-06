import os

from dotenv import load_dotenv
from openai import OpenAI

from retriever import buscar_chunks


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def responder(pergunta, chunks):

    # 1. Buscar os chunks mais relevantes
    chunks_relevantes = buscar_chunks(
        pergunta,
        chunks
    )

    # 2. Montar o contexto
    contexto = "\n\n".join(
        chunk["texto"]
        for chunk in chunks_relevantes
    )

    # 3. Montar o prompt
    prompt = f"""
Você é um assistente especializado na documentação do Mercado Pago.

Responda à pergunta utilizando somente as informações presentes no contexto abaixo.

Se a resposta não estiver no contexto, diga:
"Não encontrei essa informação na documentação fornecida."

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

RESPOSTA:
"""

    # 4. Enviar para o LLM
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text