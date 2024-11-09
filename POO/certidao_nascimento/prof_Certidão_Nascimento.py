from datetime import datetime
class Certidão_Nascimento:
  def __init__(self,nome, data_nasc,hora_nasc,cidade,estado,mae,pai="não informado"):
     self.nome = nome
     self.data_nasc = self.valida_data(data_nasc)
     self.hora_nasc = self.valida_hora(hora_nasc)
     self.cidade = cidade
     self.estado = estado
     self.mae = mae
     self.pai = pai



  def valida_data(self,data):
    # criar um try...except com a conversão do argumento
    # data em um tipo Datetime/Date
    try:
        # Tenta converter a string para um objeto datetime com o formato DD/MM/AAAA
        data = datetime.strptime(data, "%d/%m/%Y")
        return data
    except ValueError:
        # Se houver um erro de valor, a data não é válida
        #return False
        raise ValueError("Data de nascimento inválida")


  def valida_hora(self,hora):
  # criar um try...except com a conversão do argumento
  # data em um tipo Datetime/Time
    try:
      # Tenta converter a string para um objeto datetime com o formato HH:MM
      hora = datetime.strptime(hora, "%H:%M")
      return hora
    except ValueError:
      # Se houver um erro de valor, a data não é válida
      #return False
      raise ValueError("Hora de nascimento inválida")


  def __str__(self):
    saida1 = f'Nome:{self.nome}\nData de Nascimento:{datetime.strftime(self.data_nasc,"%d/%m/%Y")}'
    saida2 = f'Hora de Nascimento:{datetime.strftime(self.hora_nasc,"%H:%M")}\nCidade:{self.cidade}\nEstado:{self.estado}'
    saida3 = f'Nome da Mãe:{self.mae}\nNome do Pai:{self.pai}'
    saida = f'{saida1}\n{saida2}\n{saida3}'
    return saida
  
c1 = Certidão_Nascimento("Maria dos Anzois",'29/02/2024','15:59','Teresina','Piaui',"Francisca dos Anzois","João de Sousa")
print(c1)
c2 = Certidão_Nascimento("Ana Clara dos Anjos",'31/03/2024','00:55','Timon','Maranhão',"Maria dos Anjos")
print(c2)