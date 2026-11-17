import pytest
import app as sistema


@pytest.fixture
def cliente():
    sistema.app.config["TESTING"] = True

    with sistema.app.test_client() as cliente:
        yield cliente


def test_pagina_inicial(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200


def test_pagina_cadastro(cliente):
    resposta = cliente.get("/livros/cadastrar")
    assert resposta.status_code == 200


def test_pagina_consulta(cliente):
    resposta = cliente.get("/livros")
    assert resposta.status_code == 200


def test_pagina_emprestimo(cliente):
    resposta = cliente.get("/emprestimo")
    assert resposta.status_code == 200


def test_pagina_devolucao(cliente):
    resposta = cliente.get("/devolucao")
    assert resposta.status_code == 200
