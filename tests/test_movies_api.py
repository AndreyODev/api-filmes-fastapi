import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_root_endpoint_returns_ok():
    response = client.get("/")
    assert response.status_code == 200


def test_movie_crud_flow():
    payload = {"titulo": "Matrix"}

    create_response = client.post("/movie", json=payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["titulo"] == "Matrix"

    list_response = client.get("/movie")
    assert list_response.status_code == 200
    assert any(movie["titulo"] == "Matrix" for movie in list_response.json())

    movie_id = created["id"]
    get_response = client.get(f"/movie/{movie_id}")
    assert get_response.status_code == 200
    assert get_response.json()["titulo"] == "Matrix"

    update_response = client.put(f"/movie/{movie_id}", json={"titulo": "Matrix Reloaded"})
    assert update_response.status_code == 200
    assert update_response.json()["titulo"] == "Matrix Reloaded"

    delete_response = client.delete(f"/movie/{movie_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Filme excluído com sucesso"
