import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CATALOG_PATH = BASE_DIR / "data" / "catalog.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)


def search_catalog(intent, top_k=5):

    role = intent.get("role", "").lower()
    seniority = intent.get("seniority", "").lower()

    results = []

    for item in catalog:

        text = f"""
        {item.get('name', '')}
        {item.get('description', '')}
        {' '.join(item.get('job_levels', []))}
        {' '.join(item.get('keys', []))}
        """.lower()

        score = 0

        # Role matching
        role_words = role.split()

        for word in role_words:
            if word in text:
                score += 2

        # Seniority matching
        if seniority:
            if seniority in text:
                score += 3

        if score > 0:
            results.append((score, item))

    results.sort(key=lambda x: x[0], reverse=True)

    final_results = []

    for _, item in results[:top_k]:

        final_results.append({
            "name": item["name"],
            "url": item["link"],
            "test_type": (
                item["keys"][0]
                if item.get("keys")
                else "Unknown"
            )
        })

    return final_results