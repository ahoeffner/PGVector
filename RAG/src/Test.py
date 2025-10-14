from src.app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    print("Health check response:", r.json())


if __name__ == "__main__":
	 test_health()