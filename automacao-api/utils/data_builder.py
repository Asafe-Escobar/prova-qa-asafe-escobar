import random
import time

def gerar_id_unico() -> int:
    return int(time.time() * 1000) + random.randint(1, 999)

def novo_pet(nome: str = "rex", status: str ="available")->dict:
    return{
        "id": gerar_id_unico(),
        "category": {"id": 1, "name": "cachorros"},
        "name": nome,
        "photoUrls": ["https://exemplo.com/foto.jpg"],
        "tags": [{"id": 1, "name": "amigavel"}],
        "status": status,
    }


def novo_usuario(username: str = None) -> dict:
    if username is None:
        username = f"user_{gerar_id_unico()}"
    return {
        "id": gerar_id_unico(),
        "username": username,
        "firstName": "Joao",
        "lastName": "Silva",
        "email": f"{username}@teste.com",
        "password": "senha123",
        "phone": "86999999999",
        "userStatus": 1,
    }


def novo_pedido(pet_id: int = None) -> dict:
    if pet_id is None:
        pet_id = gerar_id_unico()
    return {
        "id": gerar_id_unico(),
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2026-12-31T10:00:00.000Z",
        "status": "placed",
        "complete": True,
    }
    