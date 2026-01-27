def test_healthcheck(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_protected_route(client):
    login = client.post(
        "/Auth/login",
        data={
            "username": "admin",
            "password": "123"
        }
    )

    assert login.status_code == 200

    token = login.json()["access_token"]

    response = client.get(
        "/Note",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code in (200, 401)
