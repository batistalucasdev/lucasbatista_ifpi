class Pessoa:
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.gato = None

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
    
    def adotar_gato(self, gato):
        if not gato.tem_dono:
            self.gato = gato
            gato.tem_dono = True
        else:
            print("Gato já tem dono!")
    
class Gato:
    def __init__(self, nome, peso, idade, raca):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__raca = raca
        self.__tem_dono = False

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
    
    @property
    def tem_dono(self):
        return self.__tem_dono
    
    @tem_dono.setter
    def tem_dono(self, gato):
        self.__tem_dono = gato

    
mimi = Gato("Sem nome", 2, 1, "Não definido")
joao = Pessoa("João Python", "Avenida X, 48", "123.456.789-00")
joao.adotar_gato(mimi)
joao.gato.nome = "Gatoso"
print(joao.gato.nome)
maria = Pessoa("Maria Zinha", "Rua 5, 2452", "793.982.129-87")
print(maria.gato)
gatrim = Gato("Gatrim", 1, 0.5, "Não definido")
joao.adotar_gato(gatrim)
print(joao.gato.nome)
maria.adotar_gato(gatrim)
print(maria.gato.nome)