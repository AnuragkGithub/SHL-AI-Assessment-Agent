import json
import faiss
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent

CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
INDEX_PATH = BASE_DIR / "data" / "catalog.index"

model = SentenceTransformer("all-MiniLM-L6-v2")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

index = faiss.read_index(str(INDEX_PATH))


def search_catalog(intent, top_k=10):

    query = f"""
    {intent.get('role', '')}
    {intent.get('seniority', '')}
    """

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    seniority = intent.get("seniority", "").lower()

    for idx in indices[0]:

        if idx >= len(catalog):
            continue

        item = catalog[idx]

        job_levels = " ".join(
            item.get("job_levels", [])
        ).lower()

        # Seniority filtering
        if seniority == "senior":
    
          blocked_levels = [
        "entry-level",
        "graduate",
        "entry level",
        "junior"
    ]

          if any(level in job_levels for level in blocked_levels):
            continue

        results.append({
            "name": item["name"],
            "url": item["link"],
            "test_type": (
                item["keys"][0]
                if item.get("keys")
                else "Unknown"
            )
        })

    return results