import re

import numpy as np
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

import spacy

def chunk_document(text: str, chunk_size=500, overlap=100) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if end < len(text):
            last_period = cheunk.rfind(".")
            if last_period > chunk_size * 0.7:
                chunk = chunk[:last_period + 1]
                end = start + last_period + 1

        chunks.append(chunk.strip())
        start = end - overlap

    return chunks


# def semantic_chunk(
#     text: str,
#     similarity_threshold: float = 0.70,
#     max_chars: int = 1200,
# ) -> list[str]:
#     """Divide um texto em chunks usando a similaridade semântica.

#     O texto é separado em sentenças. Um novo chunk começa quando a sentença
#     seguinte tem baixa similaridade com a anterior ou quando o limite máximo
#     de caracteres é atingido.
#     """
#     sentences = [
#         sentence.strip()
#         for sentence in re.split(r"(?<=[.!?])\s+|\n+", text)
#         if sentence.strip()
#     ]

#     if not sentences:
#         return []

#     if len(sentences) == 1:
#         return sentences

#     embedding_function = DefaultEmbeddingFunction()
#     embeddings = np.asarray(embedding_function(sentences), dtype=np.float32)

#     chunks = []
#     current_chunk = [sentences[0]]

#     for index in range(1, len(sentences)):
#         previous_embedding = embeddings[index - 1]
#         current_embedding = embeddings[index]

#         denominator = (
#             np.linalg.norm(previous_embedding) * np.linalg.norm(current_embedding)
#         )
#         similarity = 0.0 if denominator == 0 else float(
#             np.dot(previous_embedding, current_embedding) / denominator
#         )

#         candidate = " ".join(current_chunk + [sentences[index]])
#         should_split = (
#             similarity < similarity_threshold
#             or len(candidate) > max_chars
#         )

#         if should_split:
#             chunks.append(" ".join(current_chunk).strip())
#             current_chunk = [sentences[index]]
#         else:
#             current_chunk.append(sentences[index])

#     if current_chunk:
#         chunks.append(" ".join(current_chunk).strip())

#     return chunks
    
#SENTENCE-OR PARAGRAPH-BASED SPLITTING (SPACY)

nlp = spacy.load(
    "en_core_web_sm",
    disable=["ner", "tagger", "lemmatizer"]
)


def sentence_chunking(
    text: str,
    max_chars: int = 500,
    overlap: int = 1
) -> list[str]:

    doc = nlp(text)

    sentencas = [
        sent.text.strip()
        for sent in doc.sents
        if sent.text.strip()
    ]

    chunks = []
    atual = []

    for sentenca in sentencas:

        if not atual:
            atual.append(sentenca)
            continue

        candidato = " ".join(atual + [sentenca])

        if len(candidato) <= max_chars:
            atual.append(sentenca)
            continue

        chunks.append(" ".join(atual))

        # Mantém a última sentença do chunk anterior
        atual = atual[-overlap:] if overlap > 0 else []

        while atual and len(" ".join(atual + [sentenca])) > max_chars:
            atual.pop(0)

        atual.append(sentenca)

    if atual:
        chunks.append(" ".join(atual))

    return chunks


