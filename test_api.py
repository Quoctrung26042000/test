import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestIslandsAPI:
    def test_get_islands_sorted_by_distance(self):
        response = client.get("/islands/?latitude=10&longitude=20")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        assert data[0]["island_name"] == "Island1"
        assert data[1]["island_name"] == "Island2"
        assert data[2]["island_name"] == "Island3"
        assert data[0]["distance"] < data[1]["distance"] < data[2]["distance"]

    @pytest.mark.parametrize("latitude, longitude", [
        (None, 20),
        (10, None),
        ("abc", 20),
        (10, "def"),
        (1000, 20),
        (10, 2000),
    ])
    def test_invalid_input(self, latitude, longitude):
        response = client.get(f"/islands/?latitude={latitude}&longitude={longitude}")
        assert response.status_code == 422

    def test_missing_parameters(self):
        response = client.get("/islands/")
        assert response.status_code == 422
