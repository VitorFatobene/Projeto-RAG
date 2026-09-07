from pathlib import Path

from src.chunking import chunk_document
from src.pdf_loader import extrair_pdf
from src.vector_store import collection


PDF_PATH = Path(
    "documents/historia_do_vasco_10_mil_caracteres.pdf"
)

text = extrair_pdf(str(PDF_PATH))

chunks = chunk_document(text=text,chunk_size=500,overlap=50)

ids = [
    f"{PDF_PATH.stem}_chunk_{i}"
    for i in range(len(chunks))
]

metadatas = [
    {
        "source": PDF_PATH.name,
        "chunk": i
    }
    for i in range(len(chunks))
]

collection.upsert(
    ids=ids,
    documents=chunks,
    metadatas=metadatas
)

print(f"Documento: {PDF_PATH.name}")
print(f"Caracteres extraídos: {len(text)}")
print(f"Chunks armazenados: {len(chunks)}")