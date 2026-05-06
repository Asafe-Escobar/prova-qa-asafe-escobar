import pytest
from utils.data_builder import novo_pet, gerar_id_unico


class TestPet:

    def test_criar(self, api):
        payload = novo_pet(nome="Bidu")

        resposta = api.post("/pet", payload=payload)

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["id"] == payload["id"]
        assert corpo["name"] == "Bidu"
        assert corpo["status"] == "available"

    def test_buscar(self, api):
        payload = novo_pet(nome="Toto")
        api.post("/pet", payload=payload)

        resposta = api.get(f"/pet/{payload['id']}")

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["id"] == payload["id"]
        assert corpo["name"] == "Toto"

    def test_atualizar(self, api):
        payload = novo_pet(nome="Antigo")
        api.post("/pet", payload=payload)

        payload["name"] = "Novo"
        resposta = api.put("/pet", payload=payload)

        assert resposta.status_code == 200
        assert resposta.json()["name"] == "Novo"

    def test_deletar(self, api):
        payload = novo_pet()
        api.post("/pet", payload=payload)

        resposta = api.delete(f"/pet/{payload['id']}")

        assert resposta.status_code == 200

    def test_buscar(self, api):
        id_inexistente = gerar_id_unico()

        resposta = api.get(f"/pet/{id_inexistente}")

        assert resposta.status_code == 404