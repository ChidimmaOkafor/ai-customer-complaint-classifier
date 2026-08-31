from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_create_complaint():
    response = client.post("/complaint",
                          json={"message":"I can't access my account" }
                                              )
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert "predicted_category" in data
    assert "confidence" in data

def test_get_comlaints():
    response = client.get("/complaints")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_complaint_by_id():
    response = client.get("complaints/3")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 3
    assert "message" in data
    assert "category" in data
    assert "confidence" in data
    assert "created_at" in data

def test_invalid_complaint():
    response = client.post("/complaint",
                           json = {"message":""}
                           )
    assert response.status_code == 422