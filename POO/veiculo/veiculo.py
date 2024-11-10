'''
Exercício: Classe Veiculo
Objetivo:
Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de controle de veículos. A atividade deve explorar a criação de construtores, atributos obrigatórios e opcionais, e o uso de métodos para exibir e atualizar as informações do veículo. Requisitos:

Atributos obrigatórios:
chassi
marca (string): marca do veículo.
modelo (string): modelo do veículo.
ano (int): ano de fabricação do veículo.

Atributos opcionais:    
placa (string): placa do veículo.
cor (string): cor do veículo (padrão: "Não especificada").
proprietario (string): nome do proprietário do veículo (padrão: "Não especificado").
quilometragem (int): quilometragem atual do veículo (padrão: 0).
Especificações da Classe
Método __init__: define os atributos obrigatórios e permite incluir os opcionais com valores padrão.
Método __str__: imprime todas as informações do veículo, incluindo os atributos opcionais.
'''
class Veiculo():
    
    def __init__(self, chassi, marca, modelo, ano, placa = "Não informado", cor = "Não especificada", proprietario = "Não especificado", quilometragem = 0):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.proprietario = proprietario
        self.quilometragem = quilometragem

    def __str__(self):
        saida01 = f'Chassi: {self.chassi}'
        saida02 = f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
        saida03 = f'Placa: {self.placa}\nCor: {self.cor}\nProprietário: {self.proprietario}\nQuilometragem: {self.quilometragem}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida
    
veiculo01 = Veiculo("9BGRD08X04G117974", "Volkswagen", "Fusca", 1990, "KAJ7F26", "Cinza", "Harry Potter")
veiculo02 = Veiculo("5DM1A9TVJYNSK4443", "Audi", "A3", 2019, "AOM3X52", "Amarelo", "Saitama", "11700")
veiculo03 = Veiculo("58290YR8H89WY6640", "BYD", "Dolphin", 2024,)
print(f'{veiculo01}\n')
print(f'{veiculo02}\n')
print(f'{veiculo03}\n')