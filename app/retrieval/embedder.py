import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
INDEX_PATH = BASE_DIR / "data" / "catalog.index"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_text(item):
    
    fields = [
        item.get("name", ""),
        item.get("description", ""),
        " ".join(item.get("keys", [])),
        " ".join(item.get("job_levels", [])),
        item.get("duration", ""),
    ]

    return " ".join(fields)

def create_embeddings():
    catalog = load_catalog()

    texts = [build_text(item) for item in catalog]

    embeddings = model.encode(texts, convert_to_numpy=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, str(INDEX_PATH))

    print(f"Created embeddings for {len(catalog)} assessments")


if __name__ == "__main__":
    create_embeddings()