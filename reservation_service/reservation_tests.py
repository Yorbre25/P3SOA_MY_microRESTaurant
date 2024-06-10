import requests

def test_create_reservation():
    url = "http://localhost:8080/reservations"
    reservation_data = {
        "id": 1,
        "user_id": 123,
        "location": "Central",
        "time": "2024-06-09T19:00:00Z",
        "guests": 4
    }
    response = requests.post(url, json=reservation_data)
    assert response.status_code == 201
    print("Reservation created:", response.json())

def test_update_reservation():
    url = "http://localhost:8080/reservations/1"
    updated_data = {
        "guests": 5
    }
    response = requests.put(url, json=updated_data)
    assert response.status_code == 200
    print("Reservation updated:", response.json())

def test_delete_reservation():
    url = "http://localhost:8080/reservations/1"
    response = requests.delete(url)
    assert response.status_code == 204
    print("Reservation deleted")

if __name__ == "__main__":
    test_create_reservation()
    test_update_reservation()
    test_delete_reservation()
