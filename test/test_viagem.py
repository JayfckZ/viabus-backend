from datetime import datetime


def test_busca_viagem_por_origem(client):

    empresa = client.post(
        "/empresas",
        json={
            "nome": "Empresa X",
            "cnpj": "999",
            "email": "x@x.com",
            "telefone": "111",
        },
    ).json()

    rota = client.post(
        "/rotas",
        json={"cidade_origem": "São Paulo", "cidade_destino": "Rio de Janeiro"},
    ).json()

    onibus = client.post(
        "/onibus",
        json={
            "empresa_id": empresa["id"],
            "placa": "ABC-1234",
            "modelo": "Comil",
            "tipo_layout_assentos": "leito",
            "total_assentos": 40,
        },
    ).json()

    client.post(
        "/viagens",
        json={
            "rota_id": rota["id"],
            "onibus_id": onibus["id"],
            "data_hora_partida": datetime.utcnow().isoformat(),
            "status": "agendado",
        },
    )

    response = client.get("/viagens?origem=São")

    assert response.status_code == 200
    assert len(response.json()) > 0
