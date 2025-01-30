from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, chassi, ano):
        self._chassi = chassi
        self._ano = ano

    @abstractmethod
    def calcular_custo(self, distancia, preco_combustivel):
        pass

class Carro (Veiculo):
    def __init__(self, chassi, ano, marca_modelo):
        super().__init__(chassi, ano)
        self._marca_modelo = marca_modelo
        self._consumo_por_litro = 12

    def calcular_custo(self, distancia, preco_combustivel):
        litros_gastos = distancia/self._consumo_por_litro
        custo_total = litros_gastos * preco_combustivel
        return custo_total
    
    def __str__(self):
        return f'Carro: Chassi {self._chassi}\nAno: {self._ano}\nMarca/modelo: {self._marca_modelo}\nConsumo por litro: {self._consumo_por_litro}'
    
class Moto(Veiculo):
    def __init__(self, chassi, ano, marca_modelo):
        super().__init__(chassi, ano)
        self._marca_modelo = marca_modelo
        self._consumo_por_litro = 25

    def calcular_custo(self, distancia, preco_combustivel):
        litros_gastos = distancia/self._consumo_por_litro
        custo_total = litros_gastos * preco_combustivel
        return custo_total
    
    def __str__(self):
        return f'Moto: Chassi {self._chassi}\nAno: {self._ano}\nMarca/modelo: {self._marca_modelo}\nConsumo por litro: {self._consumo_por_litro}'
    
class Caminhao(Veiculo):
    def __init__(self, chassi, ano, marca_modelo):
        super().__init__(chassi, ano)
        self._marca_modelo = marca_modelo
        self._consumo_por_litro = 5

    def calcular_custo(self, distancia, preco_combustivel):
        litros_gastos = distancia/self._consumo_por_litro
        custo_total = litros_gastos * preco_combustivel
        return custo_total
