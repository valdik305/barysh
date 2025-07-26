import pytest
import requests


ENDPOINTS = [
    ("/categories", "GET"),
    ("/products", "GET"),
    ("/product/1/images", "GET"),
    ("/shops", "GET"),
    ("/logo/123", "GET"),
    ("/promotions", "GET"),
]

BASE_URL = "https://stage.promoductos.com.ar/api"



@pytest.mark.parametrize("path, method", ENDPOINTS)
def test_api_endpoints(path, method):
    url = f"{BASE_URL}{path}"
    try:
        response = requests.request(method, url, timeout=5)
        assert response.status_code == 200
    except requests.ConnectionError:
        pytest.fail(f"Сервер недоступен по адресу {BASE_URL}")