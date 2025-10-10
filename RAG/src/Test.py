from src.app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_health():
    r = client.get("/health")
    print("Health check response:", r.json())
    assert r.status_code == 200


def test_createEmbeddings():
    r = client.post("/createEmbeddings", json={"text": "hello"})
    print("Create Embeddings response:", r.json())
    assert r.status_code == 200
