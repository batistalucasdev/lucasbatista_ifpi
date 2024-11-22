import random
import string
from datetime import datetime, timedelta

class CartaoEmbarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data_hora_embarque):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo
        
        if len(codigo_reserva) == 6 and codigo_reserva.isalnum():
            self.codigo_reserva = codigo_reserva
        else:
            raise ValueError("O código da reserva deve ter 6 caracteres alfanuméricos.")
        
        if data_hora_embarque >= datetime.now():
            self.data_hora_embarque = data_hora_embarque
        else:
            raise ValueError("A data e hora do embarque não podem ser retroativas.")
        
        self.status_checkin = False
        self.assento = None

    def realizar_checkin(self, assentos_disponiveis):
        if self.status_checkin:
            raise ValueError("Check-in já foi realizado.")
        if not assentos_disponiveis:
            raise ValueError("Não há assentos disponíveis.")
        
        self.status_checkin = True
        self.assento = random.choice(assentos_disponiveis)
        assentos_disponiveis.remove(self.assento)
        return f"Check-in realizado com sucesso. Assento: {self.assento}"

    def alterar_assento(self, novo_assento, assentos_disponiveis):
        if not self.status_checkin:
            raise ValueError("O check-in ainda não foi realizado.")
        if novo_assento not in assentos_disponiveis:
            raise ValueError("O assento solicitado não está disponível.")
        
        assentos_disponiveis.append(self.assento)
        assentos_disponiveis.remove(novo_assento)
        self.assento = novo_assento
        return f"Assento alterado com sucesso para: {self.assento}"

# Testando a classe
def main():
    assentos_disponiveis = [f"{letra}{numero}" for letra in "ABCDEF" for numero in range(1, 11)]
    
    # Criando objetos
    try:
        voo1 = CartaoEmbarque("João Silva", "AA1234", "ABC123", datetime.now() + timedelta(hours=2))
        voo2 = CartaoEmbarque("Maria Oliveira", "BB5678", "XYZ789", datetime.now() + timedelta(hours=4))
        voo3 = CartaoEmbarque("Ana Costa", "CC9101", "QWE456", datetime.now() + timedelta(days=1))
        
        # Realizando check-ins
        print(voo1.realizar_checkin(assentos_disponiveis))
        print(voo2.realizar_checkin(assentos_disponiveis))
        print(voo3.realizar_checkin(assentos_disponiveis))
        
        # Alterando assentos
        print(voo1.alterar_assento("C5", assentos_disponiveis))
        print(voo2.alterar_assento("A2", assentos_disponiveis))
        
        # Tentando um check-in duplo
        print(voo1.realizar_checkin(assentos_disponiveis))  # Deve gerar um erro
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
