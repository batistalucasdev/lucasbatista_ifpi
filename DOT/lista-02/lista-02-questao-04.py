'''
4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.
'''

lista = []

print("Digite 15 números:")

for i in range(15):
    numero = float(input(f"Número {i + 1}: "))
    lista.append(numero)

maior = lista[0]
pos_maior = 0

menor = lista[0]
pos_menor = 0

for i in range(1, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        pos_maior = i
    if lista[i] < menor:
        menor = lista[i]
        pos_menor = i

print(f"\nMaior elemento: {maior}")
print(f"Posição do maior elemento: {pos_maior}")

print(f"\nMenor elemento: {menor}")
print(f"Posição do menor elemento: {pos_menor}")