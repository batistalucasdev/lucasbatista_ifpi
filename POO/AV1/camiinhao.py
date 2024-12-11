class Caminhão_Refrigerado:
  def __init__(self,nivel_combustivel,capacidade_carga):
     self.limite_minimo_combustivel = 0
     self.limite_maximo_combustivel = 100
     self.limite_minimo_carga = 0
     self.limite_maximo_carga = 1000
     self.limite_minimo_temperatura = -20
     self.limite_maximo_temperatura = 2
     self.nivel_combustivel = nivel_combustivel

     if 0 < capacidade_carga <= self.limite_maximo_carga:
        self.capacidade_carga = capacidade_carga
     else:
        raise ValueError("Capacidade de carga inválida")

     self.temperatura_carga = self.ajustar_temperatura(self.capacidade_carga)

  def ajustar_temperatura(self,peso_carga):
    if peso_carga <= self.limite_maximo_carga:
      percentual_carga = (peso_carga/self.capacidade_carga)*100
      if percentual_carga <= 25:
         return self.limite_maximo_temperatura
      elif 25 < percentual_carga <= 75:
         media = (self.limite_minimo_temperatura + self.limite_maximo_temperatura)/2
         return media
      elif percentual_carga > 75:
         return self.limite_minimo_temperatura
    else:
      raise ValueError("Capacidade de carga superior para os limites de temperatura!")

meu_caminhão = Caminhão_Refrigerado(100,500)
print(meu_caminhão.nivel_combustivel)
print(meu_caminhão.capacidade_carga)
print(meu_caminhão.temperatura_carga)