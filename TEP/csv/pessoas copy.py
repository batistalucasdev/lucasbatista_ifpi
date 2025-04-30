'''
Pesquisando na biblioteca oficial do python, implemente um programa para ler um arquivo .csv (Pessoas.csv) em anexo e produza os seguntes relatórios:

a) Pessoas por cidade (ex: todos de Fortaleza).
b) Pessoas com idade maior que X.
c) Pessoas entre faixas etárias.
d) Média de idade das pessoas por cidade
'''
import csv

def ler_csv(arquivo_pessoas):
    pessoas = []
    with open(arquivo_pessoas, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            linha['Idade'] = int(linha['Idade'])
            pessoas.append(linha)
    return pessoas

def pessoas_por_cidade(pessoas, cidade):
    resultado = []
    for p in pessoas:
        if p['Cidade'].lower() == cidade.lower():
            resultado.append(p)
    return resultado

def pessoas_maior_que(pessoas, idade_minima):
    resultado = []
    for p in pessoas:
        if p['Idade'] > idade_minima:
            resultado.append(p)
    return resultado

def pessoas_entre_idades(pessoas, idade_min, idade_max):
    resultado = []
    for p in pessoas:
        if idade_min <= p['Idade'] <= idade_max:
            resultado.append(p)
    return resultado

def media_idade_por_cidade(pessoas):
    cidades = {}
    for p in pessoas:
        cidade = p['Cidade']
        idade = p['Idade']
        if cidade in cidades:
            cidades[cidade].append(idade)
        else:
            cidades[cidade] = [idade]

    medias = {}
    for cidade in cidades:
        idades = cidades[cidade]
        medias[cidade] = sum(idades) / len(idades)
    return medias

pessoas = ler_csv('pessoas.csv')

print("a) Pessoas de Fortaleza:")
for p in pessoas_por_cidade(pessoas, 'Fortaleza'):
    print(p)

print("\nb) Pessoas com idade maior que 30:")
for p in pessoas_maior_que(pessoas, 30):
    print(p)

print("\nc) Pessoas entre 20 e 40 anos:")
for p in pessoas_entre_idades(pessoas, 20, 40):
    print(p)

print("\nd) Média de idade por cidade:")
medias = media_idade_por_cidade(pessoas)
for cidade in medias:
    print(f"{cidade}: {medias[cidade]:.2f} anos")
