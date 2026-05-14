from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.agent.controller import process_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return process_chat(request.messages)