'''
Exercício
Implemente uma classe que represente uma certidão de nascimento. Criar um construtor da classe. Atributos básicos: Nome, Data_nascimento, hora_nascimento, cidade, estado, Nome da mãe. Quais seriam os atributos opcionais? Crie pelo menos 2 objetos que representem essa classe e imprima seus valores.
OBS: utilizar atributos opcionais no construtor da classe
'''
from datetime import datetime

class CertidaoNascimento():
    def __init__(self, nome, data_nascimento, hora_nascimento, cidade, estado, nome_mae):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.hora_nascimento = hora_nascimento
        self.cidade = cidade
        self.estado = estado
        self.nome_mae = nome_mae

        if self.verificar_data(data_nascimento):
            print("Data válida!")
        else:
            print("Data inválida!")

        if self.verificar_hora(hora_nascimento):
            print("Hora válida!")
        else:
            print("Hora inválida!")

    def verificar_data(self, data_str):
        formato = "%d/%m/%Y"
        try:
            data_valida = datetime.strptime(data_str, formato)
            return True
        except ValueError:
            return False

    def verificar_hora(self, hora_str):
        formato = "%H:%M"
        try:
            datetime.strptime(hora_str, formato)
            return True
        except ValueError:
            return False

def main():
    certidao01 = CertidaoNascimento("Lucas Batista", "02/02/1996", "15:00", "Teresina", "Piauí", "Maria")
    print("Nome: ", certidao01.nome)
    print("Data de Nascimento: ", certidao01.data_nascimento)
    print("Hora de nascimento: ", certidao01.hora_nascimento)
    print("Cidade: ", certidao01.cidade)
    print("Estado: ", certidao01.estado)
    print("Nome da mãe: ", certidao01.nome_mae)
    print("")

    certidao02 = CertidaoNascimento("Cristiano Ronaldo", "05/02/1985", "23:99", "Ilha da Madeira", "Portugal", "Maria Dolores Aveiro")
    print("Nome: ", certidao02.nome)
    print("Data de Nascimento: ", certidao02.data_nascimento)
    print("Hora de nascimento: ", certidao02.hora_nascimento)
    print("Cidade: ", certidao02.cidade)
    print("Estado: ", certidao02.estado)
    print("Nome da mãe: ", certidao02.nome_mae)
    print("")
    
main()