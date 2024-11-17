'''
Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
possíveis. Crie objetos para testar os métodos implementados.
'''
from datetime import datetime, timedelta

class CarteiraHabilitacao:
    def __init__(self, nome, cpf, rg, categoria_cnh, data_nascimento, data_validade, data_emissao, permissao = "Não especificado"):
        self.nome = nome
        self.cpf = self.valida_cpf(cpf)
        self.rg = rg
        self.categoria_cnh = categoria_cnh
        self.data_nascimento = self.valida_data(data_nascimento)
        self.data_validade = self.valida_data(data_validade)
        self.data_emissao = self.valida_data(data_emissao)
        self.permissao = permissao

    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida")

    def valida_cpf(self, cpf):
        # Simples validação de formato (XXX.XXX.XXX-XX)
        if len(cpf) == 14 and cpf.count('.') == 2 and cpf.count('-') == 1:
            return cpf
        raise ValueError("CPF inválido. Use o formato XXX.XXX.XXX-XX.")

    def valida_tipo_cnh(self, categoria_cnh):
        categorias_validas = {'A', 'B', 'C', 'D', 'E', 'ACC'}
        if categoria_cnh in categorias_validas:
            return categoria_cnh
        raise ValueError(f'Categoria inválida.')

    def renovar_cnh(self):
        idade = (datetime.now() - self.data_nascimento).days // 365
        if idade < 50:
            nova_validade = self.data_validade + timedelta(days=365 * 10)
        else:
            nova_validade = self.data_validade + timedelta(days=365 * 5)
        self.data_validade = nova_validade
        print(f"CNH renovada. Nova data de validade: {self.data_validade.strftime('%d/%m/%Y')}")

    def mudar_categoria_cnh(self, nova_categoria):
        categorias_validas = {'A', 'B', 'C', 'D', 'E', 'ACC'}
        if nova_categoria not in categorias_validas:
            raise ValueError(f"Categoria inválida. Escolha entre {', '.join(categorias_validas)}.")
        if self.categoria_cnh == 'ACC' and nova_categoria in {'A', 'B'}:
            self.categoria_cnh = nova_categoria
        elif self.categoria_cnh == 'B' and nova_categoria in {'C', 'D', 'E'}:
            self.categoria_cnh = nova_categoria
        else:
            raise ValueError("Não é possível realizar a mudança para a categoria solicitada.")
        print(f"Categoria alterada para: {self.categoria_cnh}")

    def __str__(self):
        saida01 = f'Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}'
        saida02 = f'Data de nascimento: {datetime.strftime(self.data_nascimento,"%d/%m/%Y")}\nData de validade: {datetime.strftime(self.data_validade,"%d/%m/%Y")}\nData de emissão: {datetime.strftime(self.data_emissao,"%d/%m/%Y")}'
        saida03 = f'Categoria atual: {self.categoria_cnh}\nPermissão: {self.permissao}'
        saida = f'{saida01}\n{saida02}\n{saida03}'
        return saida
    
cnh01 = CarteiraHabilitacao("Arthur Morgan", "365.087.500-46", "50.329.075-0", "B", "02/02/1996", "14/11/2024", "18/11/2019", "Permanente")
cnh02 = CarteiraHabilitacao("John Marston", "152.476.950-97", "95.622.128-4", "ACC", "03/03/2000", "15/05/2025", "17/05/2020", "Provisória")
print(f'{cnh01}\n')

print("\nRenovando CNH...")
cnh01.renovar_cnh()

print("\nMudando categoria...")
cnh01.mudar_categoria_cnh("C")

print("\nCNH Atualizada:")
print(f'{cnh01}\n')

print("--------------------------------------------------------------------------------------------------------")

print("")
print(f'{cnh02}\n')

print("\nRenovando CNH...")
cnh02.renovar_cnh()

print("\nMudando categoria...")
cnh02.mudar_categoria_cnh("A")

print("\nCNH Atualizada:")
print(f'{cnh02}\n')