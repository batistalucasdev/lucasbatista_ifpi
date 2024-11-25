import random
from datetime import datetime, timedelta

class CartaoEmbarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data_hora_embarque):
        if len(codigo_reserva) == 6 and codigo_reserva.isalnum():
            self.__codigo_reserva = codigo_reserva
        else:
            raise ValueError("O código da reserva deve ter 6 caracteres alfanuméricos.")
        
        if data_hora_embarque >= datetime.now():
            self.__data_hora_embarque = data_hora_embarque
        else:
            raise ValueError("A data e hora do embarque não podem ser retroativas.")
        
        self.__nome_passageiro = nome_passageiro
        self.__numero_voo = numero_voo
        self.__status_checkin = False
        self.__assento = None

    # Getters para atributos imutáveis
    @property
    def nome_passageiro(self):
        return self.__nome_passageiro

    @property
    def numero_voo(self):
        return self.__numero_voo

    @property
    def codigo_reserva(self):
        return self.__codigo_reserva

    @property
    def data_hora_embarque(self):
        return self.__data_hora_embarque

    # Getters e setters para atributos mutáveis
    @property
    def status_checkin(self):
        return self.__status_checkin

    @property
    def assento(self):
        return self.__assento

    def realizar_checkin(self, assentos_disponiveis):
        if self.__status_checkin:
            raise ValueError("Check-in já foi realizado.")
        if not assentos_disponiveis:
            raise ValueError("Não há assentos disponíveis.")
        
        self.__status_checkin = True
        self.__assento = random.choice(assentos_disponiveis)
        assentos_disponiveis.remove(self.__assento)
        return f"Check-in realizado com sucesso. Assento: {self.__assento}"

    def alterar_assento(self, novo_assento, assentos_disponiveis):
        if not self.__status_checkin:
            raise ValueError("O check-in ainda não foi realizado.")
        if novo_assento not in assentos_disponiveis:
            raise ValueError("O assento solicitado não está disponível.")
        
        assentos_disponiveis.append(self.__assento)
        assentos_disponiveis.remove(novo_assento)
        self.__assento = novo_assento
        return f"Assento alterado com sucesso para: {self.__assento}"

    # Representação em string
    def __str__(self):
        checkin_status = "Realizado" if self.__status_checkin else "Não realizado"
        return (f"Passageiro: {self.__nome_passageiro}\n"
                f"Voo: {self.__numero_voo}\n"
                f"Código de Reserva: {self.__codigo_reserva}\n"
                f"Data e Hora de Embarque: {self.__data_hora_embarque}\n"
                f"Check-in: {checkin_status}\n"
                f"Assento: {self.__assento or 'Não atribuído'}\n")


# Testando a classe
assentos_disponiveis = [f"{letra}{numero}" for letra in "ABCDEF" for numero in range(1, 11)]

# Objetos de teste
voo1 = CartaoEmbarque("João Silva", "AA1234", "ABC123", datetime.now() + timedelta(hours=2))
voo2 = CartaoEmbarque("Maria Oliveira", "BB5678", "XYZ789", datetime.now() + timedelta(hours=4))
voo3 = CartaoEmbarque("Ana Costa", "CC9101", "QWE456", datetime.now() + timedelta(days=1))

# Tentativa de alterar nome do passageiro (imutável)
try:
    voo1.__nome_passageiro = "Outro Nome"
except AttributeError as e:
    print(f"Erro ao alterar nome do passageiro: {e}")

# Tentativa de alterar data do voo (imutável)
try:
    voo2.__data_hora_embarque = datetime.now() + timedelta(days=2)
except AttributeError as e:
    print(f"Erro ao alterar data do voo: {e}")

# Realizando check-in e alterando assento
print(voo1.realizar_checkin(assentos_disponiveis))
print(voo1.alterar_assento("B5", assentos_disponiveis))

# Exibindo informações dos objetos
print(voo1)
print(voo2)
print(voo3)
