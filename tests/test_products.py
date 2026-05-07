from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    
def test_post_products():
    response = client.post("/products")
    assert response.status_code == 401 
    