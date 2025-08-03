import requests

BASE_URL = "http://localhost:8080"

def test_get_all_sellers():
        response = requests.get(f"{BASE_URL}/api/seller/get_all")
        assert response.status_code == 200
        sellers = response.json()
        assert isinstance(sellers, list)
        assert len(sellers) >= 1

def test_get_seller_by_id():
    response = requests.get(f"{BASE_URL}/api/seller/get_all")
    seller_id = response.json()[0]["id"]

    response = requests.get(f"{BASE_URL}/api/seller/get?id_of_seller={seller_id}")
    assert response.status_code == 200
    seller = response.json()
    assert seller["name"] == "alex"

def test_delete_seller_add_seller():
    new_seller = {
        "name": "Удаляемый",
        "surname": "Продавец",
        "age": 25,
        "experience": 3,
        "sales": 50
    }
    response = requests.post(f"{BASE_URL}/api/seller/add", json=new_seller)
    assert response.status_code == 201
    seller_id = response.json()["id"]

    response = requests.delete(f"{BASE_URL}/api/seller/delete?id_of_seller={seller_id}")
    assert response.status_code == 204

    response = requests.get(f"{BASE_URL}/api/seller/get?id_of_seller={seller_id}")
    assert response.status_code == 404