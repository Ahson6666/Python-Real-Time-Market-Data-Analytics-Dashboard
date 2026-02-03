```python
from fastapi import FastAPI
from api import router as api_router

app = FastAPI(
    title="Real-Time Market Data Analytics Dashboard",
    version="1.0.0",
    description="HKEX market data APIs with technical indicators"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Market Data Dashboard running! HKEX live data ready."}

@app.get("/api/market/health")
async def health():
    return {"status": "healthy", "service": "HKEX market data ready"}
