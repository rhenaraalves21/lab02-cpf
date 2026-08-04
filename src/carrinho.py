class Carrinho:
    def __init__(self) -> None:
        self.itens: list[dict[str, object]] = []

    def adicionar(self, nome: str, preco: float) -> None:
        self.itens.append(
            {
                "nome": nome,
                "preco": preco,
            }
        )

    def remover(self, nome: str) -> None:
        self.itens = [
            item
            for item in self.itens
            if item["nome"] != nome
        ]

    def total(self) -> float:
        return sum(
            float(item["preco"])
            for item in self.itens
        )