'''
Utilizando o processo de abstração, implemente uma classe em Python que represente um cartão de estacionamento de shopping. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis.
Faça todas as validações possíveis. Utilize encapsulamento nos atributos necessários implementando em seguida os decoradores de leitura e/ou escrita. Crie objetos para testar os métodos implementados.

Especificações:
1. Atributos:
- Número do cartão (gerado automaticamente e composto de 8 caracteres alfanuméricos)
- Data e hora de entrada (registrada automaticamente no momento da criação do cartão)
- Status do cartão (ativo ou finalizado)
- Data e hora de saída (registrada quando o cartão é finalizado)
- Valor total (calculado no momento da saída com base no tempo de permanência e tarifa por hora)

2. Métodos sugeridos
- Um método para registrar saída, que define a data e hora de saída, altera o status para "finalizado" e calcula o valor total a ser pago.
- Um método para consultar o valor acumulado, permitindo ao cliente verificar o custo do estacionamento antes de finalizar.
- Um método para calcular o valor a ser pago, condiderando:
- Até 2h de permanência, R$ 8,00
- Acima de 2h de permanência cobrar R$ 0,50 a cada fração de 15 min

3. Requisitos de Validação:
- O número do cartão deve ser único e composto de exatamente 5 caracteres numericos.
- O status só pode ser alterado para "finalizado" se a saída for registrada.
- O tempo de permanência deve ser calculado em horas completas e frações, considerando uma tarifa fixa por hora.
- A data e hora de saída não podem ser anteriores à data e hora de entrada.

4. Teste:
- Crie pelo menos três objetos da classe, representando cartões de estacionamento diferentes.
- Demonstre os métodos implementados e suas validações em ação.
'''
from datetime import datetime

class cartaoEstacionamento():
    
    def __init__(self, numero_cartao, data_hora_entrada, status_cartao, data_hora_saida, valor_total):
        self.__numero_cartao = numero_cartao #atributo imutavel
        self.__data_hora_entrada = self.valida_data_hora(data_hora_entrada) #atributo imutavel
        self.__status_cartao = 'Ativo' #atributo mutavel
        self.__data_hora_saida = self.valida_data_hora(data_hora_saida) #atributo imutavel, registra quando o cartao é finalizado
        self.__valor_total = valor_total #atributo imutavel 
        
    @property
    def numero_cartao (self):
        return self.__numero_cartao
        
    @property
    def data_hora_entrada(self):
        return self.__data_hora_entrada

    def valida_data_hora (self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de entrada inválida")
    
    def valida_hora (self, hora):
        try:
            hora = datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            raise ValueError("Hora de entrada inválida")
    
    @property
    def status_cartao (self):
        return self.__status_cartao
    
    @property
    def valor_total(self):
        return self.__valor_total

    def registrar_saida(self):
        if self.__status == "Finalizado":
            print("O cartão já foi finalizado.")
            return
        
        self.__data_hora_saida = datetime.now()
        tempo_permanencia = self.__data_hora_saida - self.__data_hora_entrada
        horas = tempo_permanencia.total_seconds() / 3600

        if horas <= 2:
            self.__valor_total = 8.0
        else:
            self.__valor_total = 8.0 + ((horas - 2) * 4)
        
        self.__status = "Finalizado"
        print(f"Saída registrada. Valor total: R$ {self.__valor_total:.2f}")
     
    @property
    def data_hora_saida(self):
        return self.__data_hora_saida
    
    def valida_data (self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de saída inválida")
    
    def valida_hora (self, hora):
        try:
            hora = datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            raise ValueError("Hora de saída inválida")