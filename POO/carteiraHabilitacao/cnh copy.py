'''
Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
possíveis. Crie objetos para testar os métodos implementados.
'''
from datetime import datetime

class CarteiraHabilitacao:
    def __init__(self, nome, cpf, rg, categoria_cnh, data_nascimento, data_validade, data_emissao, permissao = "Não especificado"):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.categoria_cnh = categoria_cnh
        self.data_nascimento = self.valida_data(data_nascimento)
        self.data_validade = data_validade
        self.data_emissao = data_emissao
        self.permissao = permissao
        #os metodos validadores serao chamados aqui
        pass

    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida")
        #converter a string data em um tipo Date/Datetime
        # se a conversao falhar, levantar uma exceçao (raise ValueError(<mensagem>))
        #se a conversao passar, retornar a data convertida
        

    def valida_tipo_cnh(self, tipo):
        #verificar se o tipo está entre o conjunto válido de CNHs
        #se sim, retornar o tipo, se nao, retornar exceçao
        pass

    def renovar_cnh(self):
        #se idade < 50, renovar por 10 anos
        #se nao, renovar por 5 anos
        #se idade > 50, renovar por 5 anos => alterar a data de validade
        pass

    def mudar_categoria_cnh(self, nova_categoria):
        #verificar se nova_categoria é uma categoria valida
        #verificar se é possivel a mudança
        #se sim, alterar o atributo, se nao, exibir uma mensagem de erro!
        pass

    def __str__(self):
        saida01 = f'Colocar saida aqui'
        return saida01
    

'''
        def verificar_data(self, data):
        try:
            # Tenta converter a string para um objeto datetime com o formato DD/MM/AAAA
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            # Se houver um erro de valor, a data não é válida
            # return False
            raise ValueError("Data de nascimento inválida")

'''