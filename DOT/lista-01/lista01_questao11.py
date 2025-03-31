'''
11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
'''

def contar_divisores(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)

while True:
    try:
        numero = int(input("\nDigite um número inteiro positivo: "))
        if numero > 0:
            print(f"\nO número {numero} tem {contar_divisores(numero)} divisores.")
            break
        else:
            print("\nO número deve ser maior que 0. Digite novamente!")
    except ValueError:
        print("\nValor inválido. Digite novamente!")
