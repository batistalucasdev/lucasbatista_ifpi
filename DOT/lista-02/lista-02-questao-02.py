'''
2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.
'''
lista = []

print("Digite 10 números reais:")

for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    lista.append(numero)

qtd_negativos = 0
soma_positivos = 0

for numero in lista:
    if numero < 0:
        qtd_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"\nQuantidade de números negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
