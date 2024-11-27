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
diferentes.
- Crie pelo menos três objetos da classe, representando cartões de estacionamento
- Demonstre os métodos implementados e suas validações em ação.
'''
from datetime import datetime

class cartaoEstacionamento():
    
    def __init__(self, numero_cartao, data_entrada, hora_entrada, status_cartao, data_saida, hora_saida, valor_total):
        self.__numero_cartao = numero_cartao
        self.__data_entrada = data_entrada
        self.__hora_entrada = hora_entrada
        self.__status_cartao = status_cartao
        self.__data_saida = data_saida
        self.__hora_saida = hora_saida
        self.__valor_total = valor_total
        
    @property
    def numero_cartao (self):
        return self.__numero_cartao
        
    @property
    def data_entrada (self):
        return self.__data_entrada
    
    @property
    def hora_entrada (self):
        return self.__hora_entrada