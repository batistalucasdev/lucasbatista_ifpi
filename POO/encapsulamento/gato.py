class Gato:
    def __init__(self, peso, idade, nome = "sem nome", raca = "sem raça"):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.idade = idade

    def mudar_nome(self, nome):
        self.nome = nome

    def engordar(self, peso):
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

tom = Gato(1, 1, nome="Tom")
print("nome:{}\npeso:{}\nidade:{}".format(tom.nome, tom.peso, tom.idade))
tom.peso = 0.5
tom.idade = 20
print("nome:{}\npeso:{}\nidade:{}".format(tom.nome, tom.peso, tom.idade))