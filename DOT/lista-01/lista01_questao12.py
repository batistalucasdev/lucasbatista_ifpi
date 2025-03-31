'''
12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
'''

def somatorio(n):
    return sum(range(1, n + 1))

while True:
    try:
        numero = int(input("\nDigite um número inteiro positivo: "))
        if numero > 0:
            print(f"\nO somatório de {numero} é {somatorio(numero)}.")
            break
        else:
            print("\nO número deve ser maior que 0. Digite novamente!")
    except ValueError:
        print("\nValor inválido. Digite novamente!")
