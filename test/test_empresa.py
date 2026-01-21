def test_criar_empresa(client):
    response = client.post(
        "/empresas",
        json={
            "nome": "ViaBus",
            "cnpj": "123456789",
            "email": "contato@viabus.com",
            "telefone": "21900000000",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] is not None
    assert data["nome"] == "ViaBus"


def test_listar_empresas(client):
    response = client.get("/empresas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
