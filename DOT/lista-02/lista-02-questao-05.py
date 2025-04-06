'''
5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos.
'''

lista1 = []
lista2 = []
lista_intercalada = []

print("Digite 10 números para a primeira lista:")
for i in range(10):
    num = int(input(f"Lista 1 - Elemento {i + 1}: "))
    lista1.append(num)

print("\nDigite 10 números para a segunda lista:")
for i in range(10):
    num = int(input(f"Lista 2 - Elemento {i + 1}: "))
    lista2.append(num)

for i in range(10):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

print(f"\nLista intercalada com 20 elementos: {lista_intercalada}")