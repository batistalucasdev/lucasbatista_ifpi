#%%file test_posto_combustivel.py
import pytest
from posto_combustivel import Combustivel, Gasolina, Etanol, BombaDeCombustivel, Abastecimento, PostoDeCombustivel

def test_abastecimento_gasolina():
    gasolina = Gasolina(6.00, True)
    bomba = BombaDeCombustivel(1)
    bomba.associar_combustivel(gasolina)
    abastecimento = bomba.abastecer(20)
    assert abastecimento.valor_total == 120.00
    assert abastecimento.resumo() == "Bomba 1 (Gasolina Aditivada): 20 litros -> R$ 120.00"

def test_abastecimento_etanol():
    etanol = Etanol(4.50, "cana-de-açúcar")
    bomba = BombaDeCombustivel(2)
    bomba.associar_combustivel(etanol)
    abastecimento = bomba.abastecer(15)
    assert abastecimento.valor_total == 67.50
    assert abastecimento.resumo() == "Bomba 2 (Etanol de cana-de-açúcar): 15 litros -> R$ 67.50"

def test_bomba_sem_combustivel():
    bomba = BombaDeCombustivel(3)
    try:
        bomba.abastecer(10)
        assert False, "Esperado erro: Nenhum combustível associado à bomba."
    except ValueError as exception:
        assert str(exception) == "Nenhum combustível associado à bomba."

def test_abastecimento_com_quantidade_invalida():
    gasolina = Gasolina(6.00, False)
    bomba = BombaDeCombustivel(4)
    bomba.associar_combustivel(gasolina)
    try:
        bomba.abastecer(-5)
        assert False, "Esperado erro: Quantidade de litros deve ser maior que zero."
    except ValueError as exception:
        assert str(exception) == "Quantidade de litros deve ser maior que zero."
