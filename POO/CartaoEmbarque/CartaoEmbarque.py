'''
Utilizando o processo de abstração, implemente uma classe em Python que represente um cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.
Especificações:
1. Atributos imutáveis:
o Nome do passageiro
o Número do voo
o Código da reserva (localizador)
o Data e hora do embarque (utilizar biblioteca datetime para validação)
2. Atributos mutáveis:
o Status do check-in (realizado ou não)
o Assento
3. Métodos sugeridos:
o Um método para realizar o check-in, que altera o status e associa um assento (aleatório) disponível ao passageiro.
o Um método para alterar o assento (apenas se o check-in já tiver sido realizado).
o Validações para garantir que assentos indisponíveis não sejam atribuídos e que o check-in só possa ser feito uma vez.
4. Requisitos de validação:
o O código da reserva deve ter 6 caracteres alfanuméricos.
o A hora do embarque não pode ser retroativa em relação ao momento de execução do código.
5. Teste:
o Crie pelo menos três objetos da classe, representando cartões de embarque diferentes.
o Demonstre os métodos implementados e suas validações em ação.
'''
import random
from datetime import datetime

class CartaoEmbarque():
    
    def __init__(self, nome, voo, localizador, data, hora, status = "Não realizado", assento = "Não especificado"):
        self.__nome = nome
        self.__voo = voo
        self.__localizador = localizador
        self.__data = self.valida_data(data)
        self.hora = hora
        self.__status = status
        self.__assento = assento

    @property
    def nome (self):
        return self.__nome
    
    @property
    def voo (self):
        return self.__voo
    
    @property
    def localizador (self):
        return self.__localizador
    
    @property
    def data (self):
        return self.__data
    
    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de voo inválida")

    @property    
    def status (self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status
    
    @property    
    def assento (self):
        return self.__assento
    
    def realiza_checkin(self, assentos_disponiveis):
        if self.__status:
            raise ValueError("O check-in já foi realizado.")
        if not assentos_disponiveis:
            raise ValueError("Náo há assentos disponíveis.")
        
        self.__status = True
        self.assento = random.choice(assentos_disponiveis)
        assentos_disponiveis.remove(self.__assento)
        return f"O chech-in foi realizado com sucesso. Assento: {self.__assento}"
        
    def altera_assento():
        pass
'''
    def __str__(self):
        saida01 = f'Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}'
        saida02 = f'Data de nascimento: {datetime.strftime(self.data_nascimento,"%d/%m/%Y")}\nData de validade: {datetime.strftime(self.data_validade,"%d/%m/%Y")}\nData de emissão: {datetime.strftime(self.data_emissao,"%d/%m/%Y")}'
        saida03 = f'Categoria atual: {self.categoria_cnh}\nPermissão: {self.permissao}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida

'''