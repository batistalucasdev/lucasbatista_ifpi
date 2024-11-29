estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

class RadioFM():
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligado = True
        self.volume = self.volume_min

        if self.antena_habilitada != False:
            self.frequencia_atual = estacoes[0]
            self.estacao_atual = estacoes['estacoe[{0}]']
            #'Cocais'

    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estacao_atual = None

    def aumentar_volume(self):
        pass
    def diminuir_volume(self):
        pass
    def mudar_frequencia(self):
        pass
    