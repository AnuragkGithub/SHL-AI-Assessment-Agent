from fastapi import FastAPI
from app.routes.chat import router

app = FastAPI(title="SHL AI Assessment Recommender")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/")
def root():
    return {
        "message": "SHL AI Assessment Agent is running"
    }