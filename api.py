from fastapi import APIRouter, HTTPException
from models import Quote, MarketSummary, Timeframe
import numpy as np
from typing import List
from datetime import datetime, timedelta

router = APIRouter()

# Mock HKEX data (HSBC + HSI)
mock_quotes = [
    Quote(
        symbol="0005.HK",  # HSBC
        timestamp=datetime.now(),
        open=67.10, high=67.80, low=66.90, close=67.45,
        volume=1250000,
        sma_20=66.85,
        ema_12=67.12
    ),
    Quote(
        symbol="^HSI",  # Hang Seng Index
        timestamp=datetime.now(),
        open=24120, high=24210, low=24080, close=24150,
        volume=85000000,
        sma_20=23890,
        ema_12=24075
    )
]

@router.get("/market/health")
async def market_health():
    return {"status": "Market data service healthy", "markets": "HKEX ready"}

@router.get("/market/hsi")
async def hsi_data() -> MarketSummary:
    hsi = next((q for q in mock_quotes if q.symbol == "^HSI"), None)
    if not hsi:
        raise HTTPException(status_code=404, detail="HSI data not found")
    
    change_pct = ((hsi.close - hsi.open) / hsi.open) * 100
    signal = "BUY" if hsi.close > hsi.sma_20 else "HOLD"
    
    return MarketSummary(
        symbol="^HSI",
        price=hsi.close,
        change_pct=round(change_pct, 2),
        sma_20=hsi.sma_20,
        volume=hsi.volume,
        signal=signal
    )

@router.get("/market/quotes/{symbol}")
async def get_quote(symbol: str) -> Quote:
    quote = next((q for q in mock_quotes if q.symbol == symbol), None)
    if not quote:
        raise HTTPException(status_code=404, detail=f"{symbol} not found")
    return quote

@router.get("/market/gainers")
async def top_gainers() -> List[MarketSummary]:
    # Mock top gainers calculation
    return [
        MarketSummary(symbol="0005.HK", price=67.45, change_pct=2.3, sma_20=66.85, volume=1250000, signal="BUY"),
        MarketSummary(symbol="0700.HK", price=128.50, change_pct=1.8, sma_20=126.90, volume=9800000, signal="BUY")
    ]
