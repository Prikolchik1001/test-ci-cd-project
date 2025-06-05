from fastapi.testclient import TestClient

from main import app


def test_get_recipes(client: TestClient):
    response = client.get("/recipe/1")
    app.dependency_overrides.clear()
    assert response.status_code == 200
