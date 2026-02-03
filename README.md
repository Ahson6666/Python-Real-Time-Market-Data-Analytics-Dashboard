# Real-Time Market Data Analytics Dashboard (Python)

**HKEX real-time market data: OHLCV, SMA/EMA, gainers/losers, technical signals.**  
*FastAPI Python portfolio for HK investment bank junior developer roles.*

## ✨ Features
- OHLCV data storage & time-series queries
- Technical indicators: SMA(20), EMA(12)
- Top gainers/losers by volume/price
- REST APIs + caching simulation
- HSI + HSBC real-time data

## 🛠 Tech Stack
FastAPI - Python 3.11 - Pydantic - NumPy - pytest - GitHub Actions CI

## 🚀 Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload

Live API: http://localhost:8000/docs (Swagger)

