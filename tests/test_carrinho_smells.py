import time

import requests

from src.carrinho import Carrinho


CARRINHO = Carrinho()


def test_tudo():
    CARRINHO.adicionar("livro", 30)
    CARRINHO.adicionar("caneta", 5)

    assert CARRINHO.total() == 35

    CARRINHO.remover("caneta")

    assert CARRINHO.total() == 30
    assert len(CARRINHO.itens) == 1

    time.sleep(2)

    resp = requests.get("https://api.exemplo.com/precos")

    assert resp.status_code == 200