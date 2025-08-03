import requests

from random import randint

BASE_URL = "http://localhost:8080"

def test_add_100_sellers():
    for i in range(1, 88):
        new_seller = {
            "name": f"Продавец_{i/5}",
            "surname": f"Фамилия_{i}",
            "age": randint(20, 50),
            "experience": randint(1, 10),
            "sales": randint(10, 200)
        }
        response = requests.post(f"{BASE_URL}/api/seller/add", json=new_seller)
        assert response.status_code == 201
        print(f"Добавлен продавец {i} с ID: {response.json()['id']}")