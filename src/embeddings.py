import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def gerar_embedding(texto):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texto
    )

    return response.data[0].embedding


def adicionar_embeddings(chunks):

    for chunk in chunks:
        chunk["embedding"] = gerar_embedding(
            chunk["texto"]
        )

    return chunks