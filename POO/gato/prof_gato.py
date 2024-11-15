class Gato:
    def __init__(self, peso, idade, nome = "Sem nome", raca = "Sem raça"):
        self.peso = peso
        self.idade = idade
        self.nome = nome
        self.raca = raca

    def mudar_nome(self, nome):
        self.nome = nome

    def engordar(self, peso):
        self.peso += peso

    def envelhecer(self, idade):
        self.idade += 1