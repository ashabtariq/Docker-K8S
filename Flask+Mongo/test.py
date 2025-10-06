import pytest
from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


# Mock MongoDB collection using MagicMock
@pytest.fixture
def mock_collection():
    with patch("app.collection") as mock:
        yield mock


def test_get_items_empty(client, mock_collection):
    mock_collection.find.return_value = []
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json == []


def test_create_item(client, mock_collection):
    mock_collection.insert_one.return_value = MagicMock(inserted_id="123abc")
    response = client.post("/items", json={"name": "Book", "price": 20})
    assert response.status_code == 201
    assert "inserted_id" in response.json


def test_create_item_no_data(client):
    response = client.post("/items", data={})
    assert response.status_code == 400
    assert "error" in response.json


def test_get_item_found(client, mock_collection):
    mock_collection.find_one.return_value = {"_id": "507f1f77bcf86cd799439011", "name": "Phone"}
    response = client.get("/items/507f1f77bcf86cd799439011")
    assert response.status_code == 200
    assert response.json["name"] == "Phone"


def test_get_item_not_found(client, mock_collection):
    mock_collection.find_one.return_value = None
    response = client.get("/items/507f1f77bcf86cd799439011")
    assert response.status_code == 404
    assert "error" in response.json
