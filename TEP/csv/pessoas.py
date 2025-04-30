'''
Pesquisando na biblioteca oficial do python, implemente um programa para ler um arquivo .csv (Pessoas.csv) em anexo e produza os seguntes relatórios:

a) Pessoas por cidade (ex: todos de Fortaleza).
b) Pessoas com idade maior que X.
c) Pessoas entre faixas etárias.
d) Média de idade das pessoas por cidade
'''

import csv
with open ('pessoas.csv', newline='') as csvfile:
    leitura = csv.reader(csvfile)
    leitura.__next__()
    for dados in leitura:
        print(', '.join(dados))

'''
pessoas = []
with open('pessoas.csv', newline='') as csvfile:
    leitura = csv.DictReader(csvfile)
    for linha in leitura
'''

def pessoas_por_cidade(pessoas, cidade):
    return [p for p in pessoas if p[2].lower() == cidade.lower()]

cidade = input("Digite o nome da cidade: ")
print(pessoas_por_cidade(pessoas, cidade))

