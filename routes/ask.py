from fastapi import APIRouter, Body
from services.ollama_service import query_ollama

router = APIRouter()

@router.post("/ask")
async def ask_ollama(question: str = Body(..., embed=True)):
    return {"response": query_ollama(question)}
