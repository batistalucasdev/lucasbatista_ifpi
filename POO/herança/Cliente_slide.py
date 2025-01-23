class Cliente:
    def __init__(self, pais, DataCadastro):
        self.pais = pais
        self.DataCadastro= DataCadastro

class PessoaFisica(Cliente):
    def __init__(self, pais, DataCadastro, nome, sobrenome, cpf):
        super().__init__(pais, DataCadastro)
        self.nome = nome
        self.sobrenome= sobrenome
        self.cpf= cpf

class PessoaJuridica(Cliente):
    def __init__(self, pais, DataCadastro, razaosocial, nomefantasia, cnpj):
        super().__init__(pais, DataCadastro)
        self.razaosocial = razaosocial
        self.nomefantasia= nomefantasia
        self.cnpj= cnpj

maria = PessoaFisica("Brasil", "22/01/2025","Maria", "Alves", "54814293308")
google = PessoaJuridica("EUA", "09/08/2003","Google", "Alves", "12345678000195")
print(maria.pais)
print(google.pais)