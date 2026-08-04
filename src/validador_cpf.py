def remover_nao_digitos(valor: str) -> str:
    return "".join(c for c in valor if c.isdigit())


def calcular_digito(base: list[int], pesos: list[int]) -> int:
    soma = sum(b * p for b, p in zip(base, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def eh_cpf_valido(cpf: str) -> bool:
    digitos = remover_nao_digitos(cpf)

    if len(digitos) != 11:
        return False

    if len(set(digitos)) == 1:
        return False

    base = [int(d) for d in digitos[:9]]

    d1 = calcular_digito(
        base,
        list(range(10, 1, -1)),
    )

    d2 = calcular_digito(
        base + [d1],
        list(range(11, 1, -1)),
    )

    return [d1, d2] == [
        int(digitos[9]),
        int(digitos[10]),
    ]