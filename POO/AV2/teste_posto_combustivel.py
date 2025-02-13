#%%file test_posto_combustivel.py

from pytest import approx
import sys
sys.path.append('/content')
from posto_combustivel import Gasolina, Etanol, BombaDeCombustivel

def test_abastecimento_gasolina():
    gasolina = Gasolina(6.00, True)
    bomba = BombaDeCombustivel(1)
    bomba.associar_combustivel(gasolina)
    abastecimento = bomba.realizar_abastecimento(20)
    assert abastecimento.get_valor_total() == 126.00  # 6.00 * 20 * 1.05
    assert str(abastecimento) == "Bomba 1 (Gasolina Aditivada - Preço por litro: R$ 6.00): 20 litros -> R$ 126.00"

def test_abastecimento_minimo():
    gasolina = Gasolina(6.00, False)
    bomba = BombaDeCombustivel(4)
    bomba.associar_combustivel(gasolina)
    abastecimento = bomba.realizar_abastecimento(0.1)
    assert abastecimento.get_valor_total() == approx(0.60)  # 6.00 * 0.1
    assert str(abastecimento) == "Bomba 4 (Gasolina Comum - Preço por litro: R$ 6.00): 0.1 litros -> R$ 0.60"

def test_abastecimento_etanol():
    etanol = Etanol(4.50, "cana-de-açúcar")
    bomba = BombaDeCombustivel(2)
    bomba.associar_combustivel(etanol)
    abastecimento = bomba.realizar_abastecimento(15)
    assert abastecimento.get_valor_total() == 67.50
    assert str(abastecimento) == "Bomba 2 (Etanol de cana-de-açúcar - Preço por litro: R$ 4.50): 15 litros -> R$ 67.50"

def test_abastecimento_etanol_milho():
    etanol = Etanol(4.30, "milho")
    bomba = BombaDeCombustivel(3)
    bomba.associar_combustivel(etanol)
    abastecimento = bomba.realizar_abastecimento(10)
    assert abastecimento.get_valor_total() == 43.00
    assert str(abastecimento) == "Bomba 3 (Etanol de milho - Preço por litro: R$ 4.30): 10 litros -> R$ 43.00"

def test_bomba_sem_combustivel():
    bomba = BombaDeCombustivel(3)
    try:
        bomba.realizar_abastecimento(10)
        assert False, "Esperado erro: Bomba sem combustível associado."
    except ValueError as exception:
        assert str(exception) == "Bomba sem combustível associado."

def test_abastecimento_com_quantidade_invalida():
    gasolina = Gasolina(6.00, False)
    bomba = BombaDeCombustivel(4)
    bomba.associar_combustivel(gasolina)
    try:
        bomba.realizar_abastecimento(-5)
        assert False, "Esperado erro: Quantidade de litros inválida."
    except ValueError as exception:
        assert str(exception) == "Quantidade de litros inválida."

def test_abastecimento_zero_litros():
    gasolina = Gasolina(6.00, False)
    bomba = BombaDeCombustivel(5)
    bomba.associar_combustivel(gasolina)
    try:
        bomba.realizar_abastecimento(0)
        assert False, "Esperado erro: Quantidade de litros inválida."
    except ValueError as exception:
        assert str(exception) == "Quantidade de litros inválida."
