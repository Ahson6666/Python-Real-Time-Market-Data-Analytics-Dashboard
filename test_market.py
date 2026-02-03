import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_market_health():
    response = client.get("/api/market/health")
    assert response.status_code == 200
    assert "HKEX" in response.json()["markets"]

def test_hsi_data():
    response = client.get("/api/market/hsi")
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "^HSI"
    assert "sma_20" in data
    assert isinstance(data["change_pct"], (int, float))

def test_quote_endpoint():
    response = client.get("/api/market/quotes/0005.HK")
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "0005.HK"
    assert all(key in data for key in ["open", "high", "low", "close", "volume"])

def test_top_gainers():
    response = client.get("/api/market/gainers")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert all("signal" in item for item in data)
