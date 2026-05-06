import pytest
from utils.data_builder import novo_pedido, gerar_id_unico


class TestStore:

    def test_criar(self, api):
        payload = novo_pedido()

        resposta = api.post("/store/order", payload=payload)

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["id"] == payload["id"]
        assert corpo["status"] == "placed"
        assert corpo["complete"] is True

    def test_buscar_pedido_existente_retorna_dados_corretos(self, api):
        payload = novo_pedido()
        api.post("/store/order", payload=payload)

        resposta = api.get(f"/store/order/{payload['id']}")

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["id"] == payload["id"]
        assert corpo["petId"] == payload["petId"]

    def test_deletar(self, api):
        payload = novo_pedido()
        api.post("/store/order", payload=payload)

        resposta = api.delete(f"/store/order/{payload['id']}")

        assert resposta.status_code == 200

    def test_buscar_pedido_inexistente_retorna_404(self, api):
        id_inexistente = gerar_id_unico()

        resposta = api.get(f"/store/order/{id_inexistente}")

        assert resposta.status_code == 404

    def test_consultar(self, api):
        resposta = api.get("/store/inventory")

        assert resposta.status_code == 200
        corpo = resposta.json()
        assert isinstance(corpo, dict)
        assert len(corpo) > 0