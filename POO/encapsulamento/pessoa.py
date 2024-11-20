class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def getnome(self):
        return self.__nome

eu = Pessoa("Ivo")
eu.nome = "Maria"
print(eu.nome)
print(eu.getnome())