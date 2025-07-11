from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()

# Allow frontend to access backend APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body for /api/ask
class AskRequest(BaseModel):
    question: str

# Supported crypto symbols and CoinGecko mapping
SUPPORTED_SYMBOLS = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "solana": "solana",
}

# Real-time price fetch from CoinGecko
@app.get("/api/price/{symbol}")
async def get_price(symbol: str):
    symbol = symbol.lower()
    if symbol not in SUPPORTED_SYMBOLS:
        return {"error": f"Unsupported symbol '{symbol}'"}
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={SUPPORTED_SYMBOLS[symbol]}&vs_currencies=usd"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    return {symbol: {"usd": data[SUPPORTED_SYMBOLS[symbol]]["usd"]}}

# Market AI Q&A via Ollama (running on Windows host)
@app.post("/api/ask")
async def ask_question(payload: AskRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://192.168.29.35:11434/api/generate",  # Windows IP
                json={
                    "model": "mistral",
                    "prompt": payload.question,
                    "stream": False
                },
                timeout=60
            )
            result = response.json()
            return {"answer": result.get("response", "No answer")}
    except Exception as e:
        return {"error": str(e)}
