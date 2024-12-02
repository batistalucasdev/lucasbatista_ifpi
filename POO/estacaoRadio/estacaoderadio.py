class RadioFM:
    def __init__(self, vol_max, estacoes):
        self._volume_min = 0
        self._volume_max = vol_max
        self._freq_min = 88
        self._freq_max = 108
        self._estacoes = estacoes
        self._volume = None
        self._ligado = False
        self._estacao_atual = None
        self._frequencia_atual = None
        self._antena_habilitada = False

    def ligar(self):
        self._ligado = True
        self._volume = self._volume_min
        if self._antena_habilitada and self._estacoes:
            for freq in self._estacoes: 
                self._frequencia_atual = freq
                self._estacao_atual = self._estacoes[freq]
                break 

    def desligar(self):
        self._ligado = False
        self._volume = None
        self._frequencia_atual = None
        self._estacao_atual = None

    def aumentar_volume(self, incremento=1):
        if self._ligado and self._volume is not None:
            self._volume = min(self._volume + incremento, self._volume_max)

    def diminuir_volume(self, decremento=1):
        if self._ligado and self._volume is not None:
            self._volume = max(self._volume - decremento, self._volume_min)

    def mudar_frequencia(self, nova_frequencia=0):
        if not self._ligado:
            return
        if nova_frequencia and nova_frequencia in self._estacoes:
            self._frequencia_atual = nova_frequencia
            self._estacao_atual = self._estacoes[nova_frequencia]
        elif nova_frequencia:
            self._frequencia_atual = nova_frequencia
            self._estacao_atual = "estação inexistente"
        else:
            frequencias = list(self._estacoes.keys())
            if self._frequencia_atual in frequencias:
                index_atual = frequencias.index(self._frequencia_atual)
                if index_atual < len(frequencias) - 1:
                    self._frequencia_atual = frequencias[index_atual + 1]
                else:
                    self._frequencia_atual = frequencias[0]
            else:
                self._frequencia_atual = frequencias[0]
            self._estacao_atual = self._estacoes[self._frequencia_atual]

    def habilitar_antena(self):
        self._antena_habilitada = True

    def desabilitar_antena(self):
        self._antena_habilitada = False

    def __str__(self):
        return (
            f"Rádio {'Ligado' if self._ligado else 'Desligado'} | "
            f"Volume: {self._volume} | "
            f"Frequência Atual: {self._frequencia_atual} | "
            f"Estação Atual: {self._estacao_atual}"
        )

estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

radio1 = RadioFM(10, estacoes)
radio1.habilitar_antena()
radio1.ligar()
print(radio1)
radio1.aumentar_volume(3)

radio2 = RadioFM(15, estacoes)
radio2.habilitar_antena()
radio2.ligar()
radio2.mudar_frequencia(91.5)
radio2.diminuir_volume(2)
print(radio2)

radio3 = RadioFM(20, estacoes)
radio3.ligar()
radio3.aumentar_volume(5)
radio3.mudar_frequencia(95.0)
print(radio3)
