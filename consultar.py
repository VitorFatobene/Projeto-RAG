from src.vector_store import collection


query = input("Digite sua pergunta: ")

results = collection.query(
    query_texts=[query],
    n_results=3,
    include=[
        "documents",
        "metadatas",
        "distances"
    ]
)

for position, (
    document,
    metadata,
    distance
) in enumerate(
    zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ),
    start=1
):
    similarity = 1 - distance

    print(f"\nRESULTADO {position}")
    print(f"Arquivo: {metadata['source']}")
    print(f"Chunk: {metadata['chunk']}")
    print(f"Distância: {distance:.4f}")
    print(f"Similaridade: {similarity:.4f}")
    print(document)
    print("-" * 60)