import pytest

@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 201),
])
def test_create_item_various_inputs(client, payload, expected_code):
    response = client.post("/registration", json=payload)
    assert response.status_code == expected_code

@pytest.mark.parametrize("id,expected_code", [
    (11111111111, 404),
    (1, 200),  # я уже знаю что тестовый юзер лежит под 2
    ("", 404),
])
def test_read_item(client, id, expected_code):
    response = client.get(f"/user/{id}")
    assert response.status_code == expected_code

@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 200),
])
def test_login(client, payload, expected_code):
    response = client.post("/login", json=payload)
    assert response.status_code == expected_code
    
@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 400),
    ({"user_name": "Valid name", "password": "Wrong password", "new_password": "new_password"}, 400),
    ({"user_name": "Valid name", "password": "Valid password", "new_password": "new_password"}, 200),    
])

def test_update(client, login_user_fixture, payload, expected_code):
    response = client.post("/update", json=payload)
    assert response.status_code == expected_code

def test_delete(client, login_user_fixture):
    response = client.post("/delete", json={"user_name": "Valid name", "password": "Valid password", "new_password": "new_password"})
    assert response.status_code == 204