from src.validador_cpf import eh_cpf_valido


def test_cpf_valido_com_mascara_retorna_true():
    assert eh_cpf_valido("529.982.247-25") is True