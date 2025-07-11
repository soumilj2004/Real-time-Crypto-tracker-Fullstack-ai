from fastapi import APIRouter
from services.fetcher import fetch_price

router = APIRouter()

@router.get("/price/{symbol}")
async def get_price(symbol: str):
    return await fetch_price(symbol)
