'''
Exercício
Implemente uma classe que represente uma certidão de nascimento. Criar um construtor da classe. Atributos básicos: Nome, Data_nascimento, hora_nascimento, cidade, estado, Nome da mãe. Quais seriam os atributos opcionais? Crie pelo menos 2 objetos que representem essa classe e imprima seus valores.
OBS: utilizar atributos opcionais no construtor da classe
'''
from datetime import datetime

class CertidaoNascimento():
    def __init__(self, nome, data_nascimento, hora_nascimento, cidade, estado, nome_mae, nome_pai = "Não informado"):
        self.nome = nome
        self.data_nascimento = self.verificar_data(data_nascimento)
        self.hora_nascimento = self.verificar_hora(hora_nascimento)
        self.cidade = cidade
        self.estado = estado
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai

    def verificar_data(self, data):
        try:
            # Tenta converter a string para um objeto datetime com o formato DD/MM/AAAA
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            # Se houver um erro de valor, a data não é válida
            # return False
            raise ValueError("Data de nascimento inválida")

    def verificar_hora(self, hora):
        # Tenta converter a string para um objeto datetime com o formato HH:MM
        try:
            hora = datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            # Se houver um erro de valor, a hora não é válida
            # return False
            raise ValueError("Hora de nascimento inválida")

    def __str__(self):
        saida01 = f'Nome: {self.nome}\nData de nascimento: {datetime.strftime(self.data_nascimento,"%d/%m/%Y")}'
        saida02 = f'Hora de nascimento: {datetime.strftime(self.hora_nascimento,"%H:%M")}\nCidade: {self.cidade}\nEstado: {self.estado}'
        saida03 = f'Nome da mãe: {self.nome_mae}\nNome do pai: {self.nome_pai}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida

certidao01 = CertidaoNascimento("Lucas Batista", "02/02/1996", "15:00", "Teresina", "Piauí", "Maria", "José")
print(certidao01)
print("")
certidao02 = CertidaoNascimento("Cristiano Ronaldo", "05/02/1985", "23:59", "Ilha da Madeira", "Portugal", "Maria Dolores Aveiro")
print(certidao02)