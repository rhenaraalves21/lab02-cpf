import pytest

from src.validador_cpf import eh_cpf_valido
@pytest.mark.parametrize(
    "cpf",
    [
        "111.111.111-11",
        "00000000000",
        "99999999999",
    ],
)
def test_cpf_com_todos_os_digitos_iguais_retorna_false(cpf):
    assert eh_cpf_valido(cpf) is False

def test_cpf_valido_com_mascara_retorna_true():
    assert eh_cpf_valido("529.982.247-25") is True

def test_cpf_valido_sem_mascara_retorna_true():
    assert eh_cpf_valido("52998224725") is True

def test_cpf_com_menos_de_onze_digitos_retorna_false():
    assert eh_cpf_valido("529982247") is False

def test_cpf_com_digitos_verificadores_errados_retorna_false():
    assert eh_cpf_valido("529.982.247-26") is False

def test_string_vazia_retorna_false():
    assert eh_cpf_valido("") is False

def test_cpf_com_letras_e_quantidade_incompleta_retorna_false():
    assert eh_cpf_valido("abc529982") is False