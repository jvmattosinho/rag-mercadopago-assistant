from pathlib import Path


def carregar_documentos(pasta="data/documents"):

    pasta_documentos = Path(pasta)

    documentos = []

    for arquivo in pasta_documentos.glob("*.md"):

        conteudo = arquivo.read_text(encoding="utf-8")

        documento = {
            "arquivo": arquivo.name,
            "conteudo": conteudo
        }

        documentos.append(documento)

    return documentos