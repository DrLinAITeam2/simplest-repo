import pytest
import requests
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_statuses():
    response = client.get("/statuses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "pending" in data
    assert "completed" in data

def test_get_transitions_valid():
    response = client.get("/transitions/pending")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "in_progress" in data
    assert "cancelled" in data

def test_get_transitions_invalid():
    response = client.get("/transitions/invalid")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data

def test_valid_transition():
    response = client.post("/transition", json={"current": "pending", "target": "in_progress"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["new_status"] == "in_progress"

def test_invalid_transition():
    response = client.post("/transition", json={"current": "pending", "target": "completed"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is False
    assert "error" in data

def test_transition_from_completed():
    response = client.post("/transition", json={"current": "completed", "target": "pending"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is False