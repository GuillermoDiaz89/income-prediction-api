from fastapi.testclient import TestClient
from app.main import app

"""
 🧪 Test API
 This script tests the API endpoints using FastAPI's TestClient.
 You can run it using the following command:
 python -m pytest test/test_api.py  # On Windows
"""

# Test the API using FastAPI's TestClient
client = TestClient(app)

# Test the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

# Test the predict endpoint
def test_predict():
    sample = {
        "age": 37,
        "workclass": 4,
        "fnlwgt": 284582,
        "education": 9,
        "education_num": 13,
        "marital_status": 2,
        "occupation": 2,
        "relationship": 1,
        "race": 4,
        "sex": 1,
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": 38
    }
    # Send a POST request to the /predict endpoint with the sample data
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    assert "prediction" in response.json()
