class Pessoa:
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
    
    
class Gato:
    def __init__(self, nome, peso, idade, raca):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.tutor = None

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def peso(self):
        return self.__peso

    @property
    def idade(self):
        return self.__idade
    
    @property
    def raca(self):
        return self.__raca
    
    def escolher_tutor(self, tutor):
        self.tutor = tutor
    
garfield = Gato("Urea", 5, 2, "Não definido")
jack = Pessoa("Jack", "Avenida Raul Lopes, 1000", "123.456.789-00")
garfield.escolher_tutor(jack)
print(garfield.tutor.nome)

print("")

rose = Pessoa("Rose", "Titanic, 1912", "674.527.996-35")
print(garfield.tutor)

'''
print(maria.gato)
gatrim = Gato("Gatrim", 1, 0.5, "Não definido")
joao.adotar_gato(gatrim)
print(joao.gato.nome)
maria.adotar_gato(gatrim)
print(maria.gato.nome)
'''