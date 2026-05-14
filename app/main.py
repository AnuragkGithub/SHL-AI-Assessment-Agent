from fastapi import FastAPI
from app.routes.chat import router

app = FastAPI(title="SHL AI Assessment Recommender")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}