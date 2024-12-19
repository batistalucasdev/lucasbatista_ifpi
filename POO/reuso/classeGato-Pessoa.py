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
        if type(tutor) == Pessoa: # if isintance(tutor, Pessoa):
            self.tutor = tutor
    
garfield = Gato("Urea", 5, 2, "Não definido")
jack = Pessoa("Jack", "Avenida Raul Lopes, 1000", "123.456.789-00")
garfield.escolher_tutor(jack)
print(garfield.tutor.nome)
rose = Pessoa("Rose", "Titanic, 1912", "674.527.996-35")
garfield.escolher_tutor(rose)
print(garfield.tutor.nome)
midnight = Gato("Midnight", 2, 6, "Vira lata")
midnight.escolher_tutor(jack)
print(midnight.tutor.nome)