class ControleRemoto:
    
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir o canal")   


controle_remoto01 = ControleRemoto("preto", "10cm", "2cm", "2cm")
print("CONTROLE 01")
print(controle_remoto01.cor)
controle_remoto01.passar_canal("+")

print("")
print("CONTROLE 02")
controle_remoto02 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto02.cor)
controle_remoto01.passar_canal("-")