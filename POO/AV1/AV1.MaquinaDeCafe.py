# Lucas Soares Batista e Lígia Karolinne Araújo Sousa

class MaquinaDecafe:
    def __init__(self, capacidade_reservatorio):
        self.__nivel_agua = 0
        self.__capacidade_reservatorio = capacidade_reservatorio
        self.__limite_minimo_temperatura = 70
        self.__limite_maximo_temperatura = 100
        self.__tipo_cafe = None
        self.__temperatura = 10
        self.__ligado = False

    @property
    def nivel_agua(self):
        return self.__nivel_agua

    @nivel_agua.setter
    def nivel_agua(self, quantidade):
        if 0 <= quantidade <= self.__capacidade_reservatorio:
            self.__nivel_agua = quantidade
        else:
            raise ValueError(f"O nível de água deve estar entre 0 e {self.__capacidade_reservatorio} ml.")

    @property
    def capacidade_reservatorio(self):
        return self.__capacidade_reservatorio

    @property
    def tipo_cafe(self):
        return self.__tipo_cafe

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if self.__limite_minimo_temperatura <= valor <= self.__limite_maximo_temperatura:
            self.__temperatura = valor
        else:
            raise ValueError("A temperatura deve estar entre 70 e 100 graus Celsius.")

    @property
    def ligado(self):
        return self.__ligado

    def ligar(self):
        self.__ligado = True
        print(f"Máquina {self.__ligado}.")

    def desligar(self):
        self.__ligado = False
        print(f"Máquina {self.__ligado}.")

    def adicionar_agua(self, quantidade):
        if quantidade <= 0:
            print("É preciso adicionar uma quantidade válida de água.")

        if self.__nivel_agua + quantidade > self.__capacidade_reservatorio:
            self.__nivel_agua = self.__capacidade_reservatorio
            print("Atingiu a capacidade máxima do reservatório.")
        else:
            self.__nivel_agua += quantidade
            print(f"Nível atual de água: {self.__nivel_agua} ml.")

    def aquecer_agua(self, temperatura):
        if not (self.__limite_minimo_temperatura <= temperatura <= self.__limite_maximo_temperatura):
            print(f"Temperatura fora do intervalo de {self.__limite_minimo_temperatura} a {self.__limite_maximo_temperatura} graus Celsius.")

        self.__temperatura = temperatura
        print(f"Água aquecida para {self.__temperatura} graus Celsius.")

    def selecionar_tipo(self, tipo):
        lista_tipo_cafe = ["expresso", "cappuccino", "latte"]
        if tipo.lower() not in lista_tipo_cafe:
            print("Tipo de café inválido. Escolha entre: expresso, cappuccino e latte.")
    
        self.__tipo_cafe = tipo.lower()
        print(f"Tipo de café selecionado: {self.__tipo_cafe}.")

    def preparar_cafe(self):
        if not self.__ligado:
            print("A máquina está desligada.")

        if self.__nivel_agua < 50:
            print("Água insuficiente.")

        if self.__temperatura < self.__limite_minimo_temperatura:
            print("Ajuste a temperatura.")


        if not self.__tipo_cafe:
            print("Nenhum tipo de café selecionado.")

        self.__nivel_agua -= 50
        print(f"Preparando um {self.__tipo_cafe}...")

    def estado_atual(self):
            tipo_cafe = "Nenhum"
            if self.__tipo_cafe:
                tipo_cafe = self.__tipo_cafe

            estado_maquina = "Desligada"
            if self.__ligado:
                estado_maquina = "Ligada"

            estado = (
                f"Nível de água: {self.__nivel_agua} ml\n"
                f"Temperatura: {self.__temperatura} graus Celsius\n"
                f"Tipo de café: {tipo_cafe}\n"
                f"Estado da máquina: {estado_maquina}"
            )
            return estado

maquina01 = MaquinaDecafe(1500)
maquina02 = MaquinaDecafe(1500)
maquina03 = MaquinaDecafe(1500)
print("\nINICIO:")
print(maquina01.estado_atual())
print(maquina02.estado_atual())
print(maquina03.estado_atual())


maquina01.ligar()
maquina01.adicionar_agua(120)
maquina01.aquecer_agua(83)
maquina01.selecionar_tipo("expresso")
maquina01.preparar_cafe()
print(maquina01.estado_atual())

maquina02.ligar()
maquina02.adicionar_agua(800)
maquina02.aquecer_agua(97)
maquina02.selecionar_tipo("cappuccino")
maquina02.preparar_cafe()
print(maquina02.estado_atual())

maquina03.ligar()
maquina03.adicionar_agua(170)
maquina03.aquecer_agua(90)
maquina03.selecionar_tipo("latte")
maquina03.preparar_cafe()
print(maquina03.estado_atual())

print("\nFINAL:")
print(maquina01.estado_atual())
print(maquina02.estado_atual())
print(maquina03.estado_atual())