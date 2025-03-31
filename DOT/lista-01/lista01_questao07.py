'''
7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.
'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

while True:
    try:
        numero = int(input("\nDigite um número inteiro não negativo: "))
        if numero >= 0:
            print(f"\nO fatorial de {numero} é {fatorial(numero)}")
            break
        else:
            print("\nO número deve ser maior ou igual a 0. Digite novamente!")
    except ValueError:
        print("\nValor inválido. Digite novamente!")
