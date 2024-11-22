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
        self.nome = nome
        self.voo = voo
        self.localizador = localizador
        self.data = self.valida_data(data)
        self.hora = hora
        self.status = status
        self.assento = assento

    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de voo inválida")
        
    def realiza_checkin():
        pass
        
    def altera_assento():
        pass

    def __str__(self):
        saida01 = f'Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}'
        saida02 = f'Data de nascimento: {datetime.strftime(self.data_nascimento,"%d/%m/%Y")}\nData de validade: {datetime.strftime(self.data_validade,"%d/%m/%Y")}\nData de emissão: {datetime.strftime(self.data_emissao,"%d/%m/%Y")}'
        saida03 = f'Categoria atual: {self.categoria_cnh}\nPermissão: {self.permissao}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida


'''
o Um método para realizar o check-in, que altera o status e associa um assento (aleatório) disponível ao passageiro.
o Um método para alterar o assento (apenas se o check-in já tiver sido realizado).
o Validações para garantir que assentos indisponíveis não sejam atribuídos e que o check-in só possa ser feito uma vez.
'''