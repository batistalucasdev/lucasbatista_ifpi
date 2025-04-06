'''
3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura.
'''

n = int(input("Quantos números você vai digitar? "))

lista = []

for i in range(n):
    numero = float(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

print("\nSequência de números na ordem inversa:")
for numero in reversed(lista):
    print(numero)