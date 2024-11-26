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
from datetime import datetime

class CartaoEmbarque():
    
    def __init__(self, nome, voo, localizador, data, hora, status = "Não realizado", assento = "Não especificado"):
        self.__nome = nome
        self.__voo = voo
        self.__localizador = localizador
        self.__data = self.valida_data(data)
        self.__hora = self.valida_hora(hora)
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
    def hora (self):
        return self.__hora
    
    def valida_hora (self, hora):
        try:
            hora = datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            raise ValueError("Hora de voo inválida")

    @property
    def status (self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        if novo_status not in ["Não realizado", "Realizado"]:
            raise ValueError("Status inválido! Use 'Não realizado' ou 'Realizado'.")
        self.__status = novo_status
    
    @property    
    def assento (self):
        return self.__assento

    @assento.setter
    def assento (self, novo_assento):
        if self.__status != "Realizado":
            raise ValueError("Não é possível alterar o assento antes de realizar o check-in.")
        if not novo_assento:
            raise ValueError("Assento inválido.")
        
        self.__assento = novo_assento
        
    def __str__(self):
        saida01 = f'Nome: {self.nome}\nVoo: {self.voo}\nLocalizador: {self.localizador}'
        saida02 = f'Data do voo: {datetime.strftime(self.data, "%d/%m/%Y")}\nHora do voo: {datetime.strftime(self.hora, "%H:%M")}'
        saida03 = f'Status: {self.status}\nAssento: {self.assento}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida
    
cartao01 = CartaoEmbarque("Lucas Batista", "LA3851", "ABC123", "25/11/2024", "15:00")

print(f'{cartao01}')
print("")
cartao01.status = "Realizado"
print(f'{cartao01}')
print("")
cartao01.assento = "05C"
print(f'{cartao01}')