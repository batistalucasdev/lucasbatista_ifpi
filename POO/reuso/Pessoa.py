class Pessoa:
    def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",conjuge=None,mae=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__conjuge = conjuge
        self.__pai = None
        self.__mae = None

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def altura(self):
        return self.__altura

    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def estado(self):
        return self.__estado

    @property
    def conjuge(self):
        return self.__conjuge

    @property
    def est_civil(self):
        return self.__est_civil

    @nome.setter
    def nome(self,valor):
        if self.__est_civil == "casado":
            nome_antigo = self.__nome.split(" ")
            nome_conjuge = self.__conjuge.nome.split(" ")
            novo_nome = valor.split(" ")
            for i in novo_nome:
                if (i not in nome_antigo) and (i not in nome_conjuge):
                    print("nome inválido!")
                    return
            self.__nome = valor
            print ("Alteração efetuada com sucesso!")

    def casar(self,conjuge):
        self.__est_civil = "casado"
        if type(conjuge)==Pessoa:
            self.__conjuge = conjuge
            self.__conjuge.__est_civil = "casado"
            self.__conjuge.__conjuge = self

    def casar(self, conjuge):
        if self.__est_civil not in ["solteiro", "viúvo", "divorciado"]:
            print(f"{self.__nome} não pode casar no estado civil atual: {self.__est_civil}")
        elif isinstance(conjuge, Pessoa):
            if conjuge.__est_civil not in ["solteiro", "viúvo", "divorciado"]:
                print(f"{conjuge.nome} não pode casar no estado civil atual: {conjuge.__est_civil}")
            else:
                self.__est_civil = "casado"
                self.__conjuge = conjuge
                conjuge.__est_civil = "casado"
                conjuge.__conjuge = self
                print(f"{self.__nome} e {conjuge.nome} estão casados")
        else:
            print(f"O cônjuge fornecido para casar com {self.__nome} é inválido")
    
    def ter_filhos(self, conjuge, nome_filho):
        if self.__sexo == "F" and conjuge.__sexo == "M":
            novo_filho = Pessoa(nome_filho, 0, 3.5, 0.5, "M/F", "vivo", "solteiro", None)
            return novo_filho
        else:
            print("As condições para ter filho não foram atendidas")
            return None
        
maria = Pessoa("Maria", 26, 55.3, 1.58, "F", "vivo", "solteiro", None)
joao = Pessoa("João", 27, 67.5, 1.67, "M", "vivo", "solteiro", None)
jose = Pessoa("José", 32, 83.6, 1.84, "M", "vivo", "viúvo", None)
chica = Pessoa("Francisca", 30, 62.1, 1.65, "F", "vivo,", "viúvo", None)

maria.casar(joao)
print(maria.conjuge.nome)
print(joao.conjuge.nome)
maria.casar(jose)
joao.casar(chica)
maria.casar(jose)
chica.casar(jose)
print(chica.conjuge.nome)
filho = maria.ter_filhos(joao, "Joãozinho")
print(filho.nome)