class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        a = self.__nome.split(" ")
        b = nome.split(" ")
        if a[0] == b[0]:
            self.__nome = nome
        else:
            print("primeiro nome nao pode ser alterado")

Maria = Pessoa("Maria")
print(f'Meu nome é {Maria.nome}')
Paulo = Pessoa("Paulo Pereira")
print(f'Me casei com {Paulo.nome}')
Maria.nome = 'Maria Pereira'
print(f'Agora meu nome é {Maria.nome}')
Paulo.nome = "Mario"
print(f'Meu nome é {Paulo.nome}')