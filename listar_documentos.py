from src.vector_store import collection


dados = collection.get(
    include=["metadatas"]
)

arquivos = {
    metadata.get("source")
    for metadata in dados["metadatas"]
    if metadata.get("source")
}

print("Arquivos indexados:")

for arquivo in sorted(arquivos):
    print("-", arquivo)