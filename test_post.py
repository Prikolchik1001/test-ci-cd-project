from fastapi.testclient import TestClient

from main import app


def test_get_recipes(client: TestClient):
    response = client.post(
        "/recipe",
        json={
            "name": "Пицца",
            "cooking_time": 30,
            "ingredients": "тесто колбаса грибы",
            "description": "Крутое блюдо!",
        },
    )
    data = response.json()
    app.dependency_overrides.clear()
    print(data)
    assert response.status_code == 200
    assert data['name'] == 'Пицца'
