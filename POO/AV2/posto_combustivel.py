#%%file posto_combustivel.py

class Combustivel:
    def __init__(self, preco_por_litro):
        self.preco_por_litro = preco_por_litro

    def calcular_valor(self, qtd_litros):
        return qtd_litros * self.preco_por_litro

    def __str__(self):
        return f"Preço por litro: R$ {self.preco_por_litro:.2f}"


class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        super().__init__(preco_por_litro)
        self.aditivada = aditivada

    def calcular_valor(self, qtd_litros):
        return super().calcular_valor(qtd_litros) * (1.05 if self.aditivada else 1.0)

    def __str__(self):
        return f"Gasolina {'Aditivada' if self.aditivada else 'Comum'} - {super().__str__()}"


class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        super().__init__(preco_por_litro)
        self.origem = origem

    def __str__(self):
        return f"Etanol de {self.origem} - {super().__str__()}"


class BombaDeCombustivel:
    def __init__(self, id_bomba):
        self.id_bomba = id_bomba
        self.combustivel = None

    def associar_combustivel(self, combustivel):
        self.combustivel = combustivel

    def realizar_abastecimento(self, qtd_litros):
        if self.combustivel is None:
            raise ValueError("Bomba sem combustível associado.")
        if qtd_litros <= 0:
            raise ValueError("Quantidade de litros inválida.")
        valor = self.combustivel.calcular_valor(qtd_litros)
        return Abastecimento(self, qtd_litros, valor)

    def __str__(self):
        return f"Bomba {self.id_bomba} ({'Sem combustível' if not self.combustivel else self.combustivel})"


class Abastecimento:
    def __init__(self, bomba, qtd_litros, valor_total):
        self.bomba = bomba
        self.qtd_litros = qtd_litros
        self.valor_total = valor_total

    def resumo(self):
        return f"{self}"

    def __str__(self):
        return f"Bomba {self.bomba.id_bomba} ({self.bomba.combustivel}): {self.qtd_litros} litros -> R$ {self.valor_total:.2f}"


class PostoDeCombustivel:
    def __init__(self):
        self.bombas = []

    def adicionar_bomba(self, bomba):
        self.bombas.append(bomba)

    def listar_bombas(self):
        resultado = []
        for b in self.bombas:
            resultado.append(f"Bomba {b.id_bomba}")
        return resultado

    def __str__(self):
        return "\n".join([str(b) for b in self.bombas])


if __name__ == "__main__":
    posto = PostoDeCombustivel()

    bomba1 = BombaDeCombustivel(1)
    gasolina = Gasolina(6.00, True)
    bomba1.associar_combustivel(gasolina)
    posto.adicionar_bomba(bomba1)

    bomba2 = BombaDeCombustivel(2)
    etanol = Etanol(4.50, "cana-de-açúcar")
    bomba2.associar_combustivel(etanol)
    posto.adicionar_bomba(bomba2)

    abastecimento1 = bomba1.realizar_abastecimento(20)
    abastecimento2 = bomba2.realizar_abastecimento(15)

    print("Resumo dos abastecimentos:")
    print(abastecimento1.resumo())
    print(abastecimento2.resumo())
