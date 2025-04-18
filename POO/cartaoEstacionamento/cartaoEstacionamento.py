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
import random
import string

class CartaoEstacionamento:
    def __init__(self):
        self.__numero_cartao = self.gerar_numero_cartao()
        self.__data_hora_entrada = datetime.now()
        self.__status = "Ativo"
        self.__data_hora_saida = None
        self.__valor_total = 0.0

    def gerar_numero_cartao(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def data_hora_entrada(self):
        return self.__data_hora_entrada

    @property
    def status(self):
        return self.__status

    @property
    def data_hora_saida(self):
        return self.__data_hora_saida

    @property
    def valor_total(self):
        return self.__valor_total

    def registrar_saida(self, data_hora_saida):
        if self.__status == "Finalizado":
            print("O cartão já foi finalizado.")
            return

        formatos_aceitos = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"]

        for formato in formatos_aceitos:
            try:
                data_hora_saida = datetime.strptime(data_hora_saida, formato)
                break
            except ValueError:
                continue
        else:
            print("Data/hora de saída inválida. Use o formato: YYYY-MM-DD HH:MM ou YYYY-MM-DD HH:MM:SS")
            return

        if data_hora_saida < self.__data_hora_entrada:
            print("A data/hora de saída não pode ser anterior à data/hora de entrada.")
            return

        self.__data_hora_saida = data_hora_saida

        tempo_permanencia = self.__data_hora_saida - self.__data_hora_entrada
        horas = tempo_permanencia.total_seconds() / 3600

        if horas <= 2:
            self.__valor_total = 8.0
        else:
            self.__valor_total = 8.0 + ((horas - 2) * 4)

        self.__status = "Finalizado"
        print(f"Saída registrada. Valor total: R$ {self.__valor_total:.2f}")

    def __str__(self):
        entrada_formatada = self.__data_hora_entrada.strftime("%d/%m/%Y %H:%M:%S")
        saida_formatada = self.__data_hora_saida.strftime("%d/%m/%Y %H:%M:%S") if self.__data_hora_saida else "Ainda não registrada"
        saida01 = f'Número do cartão: {self.__numero_cartao}\nData/Hora de Entrada: {entrada_formatada}'
        saida02 = f'Status: {self.__status}\nData/Hora de Saída: {saida_formatada}'
        saida03 = f'Valor Total: R$ {self.__valor_total:.2f}'
        return f'{saida01}\n{saida02}\n{saida03}'

cartao1 = CartaoEstacionamento()
print(cartao1)
cartao1.registrar_saida("2024-11-28 10:30")
print(cartao1)
print("")
cartao2 = CartaoEstacionamento()
print(cartao2)
cartao2.registrar_saida("2024-11-30 22:47")
print(cartao2)
print("")
cartao3 = CartaoEstacionamento()
print(cartao3)
cartao3.registrar_saida("2024-12-14 09:21")
print(cartao3)
print("")
