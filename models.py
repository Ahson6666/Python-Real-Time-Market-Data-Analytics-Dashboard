from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class Timeframe(str, Enum):
    M1 = "1m"
    M5 = "5m"
    H1 = "1h"
    D1 = "1d"

class Quote(BaseModel):
    symbol: str  # "0005.HK", "^HSI"
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    sma_20: Optional[float] = None
    ema_12: Optional[float] = None

class MarketSummary(BaseModel):
    symbol: str
    price: float
    change_pct: float
    sma_20: float
    volume: int
    signal: str  # "BUY", "SELL", "HOLD"
