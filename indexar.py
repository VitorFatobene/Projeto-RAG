from pathlib import Path

from src.chunking import semantic_chunk
from src.pdf_loader import extrair_txt
from src.vector_store import collection


TXT_DIR = Path("documents/txt")
txt_files = sorted(TXT_DIR.glob("*.txt"))[:100]

ids = []
documents = []
metadatas = []

for txt_path in txt_files:
    text = extrair_txt(str(txt_path))
    chunks = semantic_chunk(text=text, max_chars=1200)

    for i, chunk in enumerate(chunks):
        ids.append(f"{txt_path.stem}_chunk_{i}")
        documents.append(chunk)
        metadatas.append(
            {
                "source": txt_path.name,
                "chunk": i,
            }
        )

# Reconstrói a coleção para não misturar documentos de indexações anteriores.
existing_ids = collection.get(include=[])["ids"]
if existing_ids:
    collection.delete(ids=existing_ids)

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print(f"Documentos processados: {len(txt_files)}")
print(f"Chunks armazenados: {len(documents)}")
