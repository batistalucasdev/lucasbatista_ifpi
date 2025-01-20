import pytest
from datetime import datetime
from veiculos import Veiculo, Carro, Moto

# Testes para a classe base Veiculo
def test_veiculo_ligar():
    veiculo = Veiculo("Genérica", "Modelo", 2020, 10000)
    assert veiculo.ligar() == "O veículo está ligado."

def test_veiculo_desligar():
    veiculo = Veiculo("Genérica", "Modelo", 2020, 10000)
    assert veiculo.desligar() == "O veículo está desligado."

# Testes para a classe Carro
def test_carro_ipva_novo():
    carro = Carro("VW", "Polo", datetime.now().year, 60000, 4)
    assert carro.calcula_ipva() == 0.04 * 60000  # IPVA de 4%

def test_carro_ipva_antigo():
    carro = Carro("VW", "Fusca", 1978, 1500, 2)
    assert carro.calcula_ipva() == 0  # Carros com mais de 10 anos não pagam IPVA

def test_carro_str():
    carro = Carro("VW", "Polo", 2024, 60000, 4)
    assert "VW" in str(carro)
    assert "Polo" in str(carro)
    assert "60000" in str(carro)
    assert "IPVA" in str(carro)
    assert "4 portas" in str(carro)

# Testes para a classe Moto
def test_moto_ipva_nova():
    moto = Moto("Honda", "Pop", 2015, 10000, 100)
    assert moto.calcula_ipva() == 0.02 * 10000  # IPVA de 2%

def test_moto_ipva_antiga():
    moto = Moto("Yamaha", "XT600", 2000, 5000, 600)
    assert moto.calcula_ipva() == 0  # Motos com mais de 10 anos não pagam IPVA

def test_moto_str():
    moto = Moto("Honda", "Pop", 2015, 10000, 100)
    assert "Honda" in str(moto)
    assert "Pop" in str(moto)
    assert "10000" in str(moto)
    assert "IPVA" in str(moto)
    assert "100cc" in str(moto)

# Testando métodos herdados em Carro e Moto
def test_heranca_ligar():
    carro = Carro("VW", "Polo", 2024, 60000, 4)
    moto = Moto("Honda", "Pop", 2015, 10000, 100)
    assert carro.ligar() == "O veículo está ligado."
    assert moto.ligar() == "O veículo está ligado."
