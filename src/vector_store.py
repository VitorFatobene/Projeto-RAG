from pathlib import Path
import chromadb


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "chroma"

client = chromadb.PersistentClient(
    path=str(DATABASE_PATH)
)

collection = client.get_or_create_collection(
    name="documentos_vasco_v1",
    configuration={
        "hnsw": {
            "space": "cosine"
        }
    }
)