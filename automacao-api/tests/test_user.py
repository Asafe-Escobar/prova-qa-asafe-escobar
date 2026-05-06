import pytest
from utils.data_builder import novo_usuario


class TestUser:

    def test_criar(self, api):
        payload = novo_usuario()

        resposta = api.post("/user", payload=payload)

        assert resposta.status_code == 200

    def test_buscar(self, api):
        payload = novo_usuario()
        api.post("/user", payload=payload)

        resposta = api.get(f"/user/{payload['username']}")

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["username"] == payload["username"]
        assert corpo["email"] == payload["email"]

    def test_atualizar(self, api):
        payload = novo_usuario()
        api.post("/user", payload=payload)

        payload["firstName"] = "Maria"
        payload["lastName"] = "Souza"
        resposta = api.put(f"/user/{payload['username']}", payload=payload)

        assert resposta.status_code == 200

    def test_deletar(self, api):
        payload = novo_usuario()
        api.post("/user", payload=payload)

        resposta = api.delete(f"/user/{payload['username']}")

        assert resposta.status_code == 200

    def test_busca(self, api):
        username_inexistente = "usuario_que_nao_existe_xyz_12345"

        resposta = api.get(f"/user/{username_inexistente}")

        assert resposta.status_code == 404

    def test_login(self, api):
        payload = novo_usuario()
        api.post("/user", payload=payload)

        params = {
            "username": payload["username"],
            "password": payload["password"],
        }
        resposta = api.get("/user/login", params=params)

        assert resposta.status_code == 200
        assert "logged in user session" in resposta.text.lower()