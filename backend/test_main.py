from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is up and running!"}

def test_read_dynasties():
    response = client.get("/dynasties")
    assert response.status_code == 200

def test_read_events():
    response = client.get("/events")
    assert response.status_code == 200

def test_read_random_dynasty():
    response = client.get("/random/dynasty")
    assert response.status_code == 200

def test_read_dynasty_exist():
    response = client.get("/dynasties/japan")
    assert response.status_code == 200
    assert response.json() == {"id": 0, "house": "Yamato", "end_year": "Continue", "name": "Japan", "start_year": "660 BC", "current_country": "Japan"}

def test_read_inexistent_dynasty():
    response = client.get("/dynasties/vietnam")
    assert response.status_code == 404
    assert response.json() == {"detail": "Dynasty not found!"}
