'''
Exercício
Implemente uma classe que represente uma certidão de nascimento. Criar um construtor da classe. Atributos básicos: Nome, Data_nascimento, hora_nascimento, cidade, estado, Nome da mãe. Quais seriam os atributos opcionais? Crie pelo menos 2 objetos que representem essa classe e imprima seus valores.
OBS: utilizar atributos opcionais no construtor da classe
'''

class CertidaoNascimento():
    def __init__(self, nome, data_nascimento, hora_nascimento, cidade, estado, nome_mae):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.hora_nascimento = hora_nascimento
        self.cidade = cidade
        self.estado = estado
        self.nome_mae = nome_mae

        #dentro do init chamar a validação da data e a validacao da hora

    def verificar_data(self, data):
        #criar um try... except com a conversão do argumento
        # data em um tipo Datetime/Time
        pass

    def verificar_hora(self, hora):
        pass

def main():
    certidao01 = CertidaoNascimento("Lucas Batista", "02/02/1996", "15:00", "Teresina", "Piauí", "Maria")
    print("Nome: ", certidao01.nome)
    print("Data de Nascimento: ", certidao01.data_nascimento)
    print("Hora de nascimento: ", certidao01.hora_nascimento)
    print("Cidade: ", certidao01.cidade)
    print("Estado: ", certidao01.estado)
    print("Nome da mãe: ", certidao01.nome_mae)

main()