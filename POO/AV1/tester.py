class MaquinaDeCafe:
    def __init__(self, capacidade_reservatorio=2000):
        self.__nivel_agua = 0  # nível inicial de água
        self.__capacidade_reservatorio = capacidade_reservatorio  # capacidade máxima do reservatório
        self.__tipo_cafe = None  # tipo de café selecionado
        self.__temperatura = 25  # temperatura inicial (ambiente)
        self.__ligado = False  # estado inicial da máquina

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

    @tipo_cafe.setter
    def tipo_cafe(self, tipo):
        tipos_validos = ["expresso", "cappuccino", "latte"]
        if tipo.lower() in tipos_validos:
            self.__tipo_cafe = tipo.lower()
        else:
            raise ValueError(f"Tipo de café inválido. Escolha entre: expresso, cappuccino, latte.")

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 70 <= valor <= 100:
            self.__temperatura = valor
        else:
            raise ValueError("A temperatura deve estar entre 70 e 100 graus Celsius.")

    @property
    def ligado(self):
        return self.__ligado

    # Método para ligar a máquina
    def ligar(self):
        self.__ligado = True
        print("Máquina ligada.")

    # Método para desligar a máquina
    def desligar(self):
        self.__ligado = False
        print("Máquina desligada.")

    # Método para adicionar água
    def adicionar_agua(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida para adicionar água.")
            return

        if self.__nivel_agua + quantidade > self.__capacidade_reservatorio:
            print("Excedendo a capacidade máxima. Adicionando apenas o possível.")
            self.__nivel_agua = self.__capacidade_reservatorio
        else:
            self.__nivel_agua += quantidade
        print(f"Água adicionada. Nível atual: {self.__nivel_agua} ml.")

    # Método para aquecer a água
    def aquecer_agua(self, temperatura):
        if not (70 <= temperatura <= 100):
            print("Temperatura fora do intervalo permitido (70 a 100 graus Celsius).")
            return

        self.__temperatura = temperatura
        print(f"Água aquecida para {self.__temperatura} graus Celsius.")

    # Método para selecionar o tipo de café
    def selecionar_tipo(self, tipo):
        tipos_validos = ["expresso", "cappuccino", "latte"]
        if tipo.lower() not in tipos_validos:
            print("Tipo de café inválido. Escolha entre: expresso, cappuccino, latte.")
            return

        self.__tipo_cafe = tipo.lower()
        print(f"Tipo de café selecionado: {self.__tipo_cafe.capitalize()}.")

    def preparar_cafe(self):
        if not self.__ligado:
            print("A máquina está desligada. Ligue-a para preparar o café.")
            return

        if self.__nivel_agua < 100:
            print("Água insuficiente para preparar o café.")
            return

        if self.__temperatura < 70:
            print("A água não está na temperatura adequada para preparar o café.")
            return

        if not self.__tipo_cafe:
            print("Nenhum tipo de café selecionado. Selecione um tipo de café antes de preparar.")
            return

        self.__nivel_agua -= 100
        print(f"Preparando um {self.__tipo_cafe.capitalize()}... Pronto! Aproveite seu café.")

    # Método para retornar o estado atual
    def estado_atual(self):
        estado = {
            "Nível de água": f"{self.__nivel_agua} ml",
            "Temperatura": f"{self.__temperatura} graus Celsius",
            "Tipo de café": self.__tipo_cafe.capitalize() if self.__tipo_cafe else "Nenhum",
            "Estado da máquina": "Ligada" if self.__ligado else "Desligada"
        }
        return estado

# Simulação de uso da máquina
def simular_maquina():
    # Criando objetos
    maquina1 = MaquinaDeCafe()
    maquina2 = MaquinaDeCafe(3000)
    maquina3 = MaquinaDeCafe(1500)

    # Estados iniciais
    print("Estados iniciais:")
    print(maquina1.estado_atual())
    print(maquina2.estado_atual())
    print(maquina3.estado_atual())

    # Simulação de uso
    print("\nSimulação:")
    maquina1.ligar()
    maquina1.adicionar_agua(500)
    maquina1.aquecer_agua(85)
    maquina1.selecionar_tipo("expresso")
    maquina1.preparar_cafe()
    print(maquina1.estado_atual())

    maquina2.ligar()
    maquina2.adicionar_agua(1000)
    maquina2.aquecer_agua(95)
    maquina2.selecionar_tipo("cappuccino")
    maquina2.preparar_cafe()
    print(maquina2.estado_atual())

    maquina3.ligar()
    maquina3.adicionar_agua(200)
    maquina3.aquecer_agua(90)
    maquina3.selecionar_tipo("latte")
    maquina3.preparar_cafe()
    print(maquina3.estado_atual())

    # Estados finais
    print("\nEstados finais:")
    print(maquina1.estado_atual())
    print(maquina2.estado_atual())
    print(maquina3.estado_atual())

# Executando a simulação
simular_maquina()
