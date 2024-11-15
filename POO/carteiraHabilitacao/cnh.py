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

    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida")

    def valida_tipo_cnh(self, categoria_cnh):
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
        saida01 = f'Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\n'
        #saida02 = f'Data de nascimento: {datetime.strftime(self.data_nascimento,"%d/%m/%Y")}\nData de validade: {datetime.strftime(self.data_validade,"%d/%m/%Y")}\nData de emissão: {datetime.strftime(self.data_emissao,"%d/%m/%Y")}'
        saida03 = f'Permissão: {self.permissao}'
        #saida = f'{saida01}\n{saida02}\n{saida03}'
        saida = f'{saida01}\n{saida03}'
        return saida
    
cnh01 = CarteiraHabilitacao("Arthur Morgan", "365.087.500-46", "50.329.075-0", "B", "05/02/1987", "14/11/2024", "20/11/2019")
print(cnh01)
print("")

