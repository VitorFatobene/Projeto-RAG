def chunk_document(text: str, chunk_size = 500, overlap = 100) -> list[str]:
    chunks = []
    start = 0;

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if end < len(text):
            last_period = chunk.rfind(".")#retorna a poosição do ultimo ponto final dentro do chunk
            if last_period > chunk_size * 0.7: #verifica se o ultimo ponto está depois de 70% do chunk, se não tiver não corta o chunk pois ele ainda é mto pequeno
                chunk = chunk[:last_period + 1]#corta o chunk até o ultimo ponto. O +1 é para incluir o ponto
                end = start + last_period + 1

        chunks.append(chunk.strip())
        start = end - overlap;

    return chunks
    