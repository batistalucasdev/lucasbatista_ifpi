'''
1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.
'''

lista = list(range(100))
qtd_pares = 0
for i in lista:
    if i % 2 == 0:
        qtd_pares += 1
print(f'\na) A quatidade de números pares é {qtd_pares}')

lista_pares = []
for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
print(f'\nb) Lista com os números pares: {lista_pares}')

lista = list(range(100))
qtd_impares = 0
for i in lista:
    if i % 2 != 0:
        qtd_impares += 1
print(f'\nc) A quatidade de números ímpares é {qtd_impares}')

lista_impares = []
for numero in lista:
    if numero % 2 != 0:
        lista_impares.append(numero)
print(f'\nd) Lista com os números ímpares: {lista_impares}')