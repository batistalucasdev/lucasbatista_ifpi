#%%file posto_combustivel.py

class Combustivel:
    def __init__(self, preco_por_litro):
        self.__preco_por_litro = preco_por_litro

    def calcular_valor(self, qtd_litros):
        return qtd_litros * self.__preco_por_litro

    def get_preco_por_litro(self):
        return self.__preco_por_litro

    def set_preco_por_litro(self, novo_preco):
        if novo_preco > 0:
            self.__preco_por_litro = novo_preco
        else:
            raise ValueError("O preço por litro deve ser positivo.")

    def __str__(self):
        return f"Preço por litro: R$ {self.__preco_por_litro:.2f}"


class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        super().__init__(preco_por_litro)
        self.__aditivada = aditivada

    def calcular_valor(self, qtd_litros):
        return super().calcular_valor(qtd_litros) * (1.05 if self.__aditivada else 1.0)

    def get_aditivada(self):
        return self.__aditivada

    def __str__(self):
        return f"Gasolina {'Aditivada' if self.__aditivada else 'Comum'} - {super().__str__()}"


class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        super().__init__(preco_por_litro)
        self.__origem = origem

    def get_origem(self):
        return self.__origem

    def __str__(self):
        return f"Etanol de {self.__origem} - {super().__str__()}"


class BombaDeCombustivel:
    def __init__(self, id_bomba):
        self.__id_bomba = id_bomba
        self.__combustivel = None

    def associar_combustivel(self, combustivel):
        self.__combustivel = combustivel

    def realizar_abastecimento(self, qtd_litros):
        if self.__combustivel is None:
            raise ValueError("Bomba sem combustível associado.")
        if qtd_litros <= 0:
            raise ValueError("Quantidade de litros inválida.")
        valor = self.__combustivel.calcular_valor(qtd_litros)
        return Abastecimento(self, qtd_litros, valor)

    def get_id_bomba(self):
        return self.__id_bomba

    def get_combustivel(self):
        return self.__combustivel

    def __str__(self):
        return f"Bomba {self.__id_bomba} ({'Sem combustível' if not self.__combustivel else self.__combustivel})"


class Abastecimento:
    def __init__(self, bomba, qtd_litros, valor_total):
        self.__bomba = bomba
        self.__qtd_litros = qtd_litros
        self.__valor_total = valor_total

    def get_qtd_litros(self):
        return self.__qtd_litros

    def get_valor_total(self):
        return self.__valor_total

    def resumo(self):
        return f"{self}"

    def __str__(self):
        return f"Bomba {self.__bomba.get_id_bomba()} ({self.__bomba.get_combustivel()}): {self.__qtd_litros} litros -> R$ {self.__valor_total:.2f}"


class PostoDeCombustivel:
    def __init__(self):
        self.__bombas = []

    def adicionar_bomba(self, bomba):
        self.__bombas.append(bomba)

    def listar_bombas(self):
        return [f"Bomba {b.get_id_bomba()}" for b in self.__bombas]

    def get_bombas(self):
        return self.__bombas.copy()  # Retorna uma cópia para evitar modificações externas

    def __str__(self):
        return "\n".join([str(b) for b in self.__bombas])
