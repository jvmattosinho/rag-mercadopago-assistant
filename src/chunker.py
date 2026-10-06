def criar_chunks(documentos):

    chunks = []

    for documento in documentos:

        # Divide o conteúdo por parágrafos
        paragrafos = documento["conteudo"].split("\n\n")

        for paragrafo in paragrafos:

            paragrafo = paragrafo.strip()

            if not paragrafo:
                continue

            chunk = {
                "texto": paragrafo,
                "arquivo": documento["arquivo"]
            }

            chunks.append(chunk)

    return chunks