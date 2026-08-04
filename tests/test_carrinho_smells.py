# import time

# import requests

# from src.carrinho import Carrinho


# CARRINHO = Carrinho()


# def test_tudo():
#     CARRINHO.adicionar("livro", 30)
#     CARRINHO.adicionar("caneta", 5)

#     assert CARRINHO.total() == 35

#     CARRINHO.remover("caneta")

#     assert CARRINHO.total() == 30
#     assert len(CARRINHO.itens) == 1

#     time.sleep(2)

#     resp = requests.get("https://api.exemplo.com/precos")

#     assert resp.status_code == 200

import pytest

from src.carrinho import Carrinho


@pytest.fixture
def carrinho():
    return Carrinho()


def test_carrinho_novo_tem_total_zero(carrinho):
    assert carrinho.total() == 0


def test_adicionar_dois_itens_atualiza_total(carrinho):
    carrinho.adicionar("livro", 30)
    carrinho.adicionar("caneta", 5)

    assert carrinho.total() == 35


def test_remover_item_atualiza_total(carrinho):
    carrinho.adicionar("livro", 30)
    carrinho.adicionar("caneta", 5)

    carrinho.remover("caneta")

    assert carrinho.total() == 30