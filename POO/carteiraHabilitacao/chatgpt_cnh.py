from datetime import datetime, timedelta

class CarteiraHabilitacao:
    def __init__(self, nome, cpf, rg, categoria_cnh, data_nascimento, data_validade, data_emissao, permissao="Não especificado"):
        self.nome = nome
        self.cpf = self.valida_cpf(cpf)
        self.rg = rg
        self.categoria_cnh = self.valida_tipo_cnh(categoria_cnh)
        self.data_nascimento = self.valida_data(data_nascimento)
        self.data_validade = self.valida_data(data_validade)
        self.data_emissao = self.valida_data(data_emissao)
        self.permissao = permissao

    def valida_data(self, data):
        try:
            return datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")

    def valida_cpf(self, cpf):
        # Simples validação de formato (XXX.XXX.XXX-XX)
        if len(cpf) == 14 and cpf.count('.') == 2 and cpf.count('-') == 1:
            return cpf
        raise ValueError("CPF inválido. Use o formato XXX.XXX.XXX-XX.")

    def valida_tipo_cnh(self, categoria_cnh):
        categorias_validas = {'A', 'B', 'C', 'D', 'E', 'ACC'}
        if categoria_cnh in categorias_validas:
            return categoria_cnh
        raise ValueError(f"Categoria inválida. Escolha entre {', '.join(categorias_validas)}.")

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
        saida01 = f'Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\n'
        saida02 = f'Data de nascimento: {self.data_nascimento.strftime("%d/%m/%Y")}\n'
        saida03 = f'Data de validade: {self.data_validade.strftime("%d/%m/%Y")}\nData de emissão: {self.data_emissao.strftime("%d/%m/%Y")}\n'
        saida04 = f'Categoria: {self.categoria_cnh}\nPermissão: {self.permissao}'
        return f'{saida01}{saida02}{saida03}{saida04}'


# Teste
cnh01 = CarteiraHabilitacao(
    nome="Arthur Morgan", 
    cpf="365.087.500-46", 
    rg="50.329.075-0", 
    categoria_cnh="B", 
    data_nascimento="05/02/1987", 
    data_validade="14/11/2024", 
    data_emissao="20/11/2019"
)

cnh02 = CarteiraHabilitacao(
    nome="Maria Francisca Raimunda",
    cpf="003.832.720-17", 
    rg="14.286.345-2", 
    categoria_cnh="A", 
    data_nascimento="28/02/1991", 
    data_validade="14/11/2024", 
    data_emissao="20/11/2019"
)

print(cnh01)
print("\nRenovando CNH...")
cnh01.renovar_cnh()

print("\nMudando categoria...")
cnh01.mudar_categoria_cnh("C")

print("\nCNH Atualizada:")
print(cnh01)

print("")

print(cnh02)
print("\nRenovando CNH...")
cnh02.renovar_cnh()

#print("\nMudando categoria...")
#cnh02.mudar_categoria_cnh("B")

print("\nCNH Atualizada:")
print(cnh02)
